#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <mosquitto.h>
#include <mysql.h>
#include <json-c/json.h>

#define TOPIC "sensor/dht"
#define BROKER "localhost"
#define PORT 1883
#define MOSQoS 1

MYSQL *conn;

void insertar_datos(const char *timestamp, float temp, float hum) {
    char query[512];

    snprintf(
        query,
        sizeof(query),
        "INSERT INTO dht_data (timestamp, temperatura, humedad) "
        "VALUES ('%s', %.2f, %.2f)",
        timestamp,
        temp,
        hum
    );

    if (mysql_query(conn, query)) {
        fprintf(stderr, "[MySQL] Error: %s\n", mysql_error(conn));

    } else {
        printf("[MySQL] Insertado.\n");
    }
}

void on_message(
    struct mosquitto *mosq,
    void *userdata,
    const struct mosquitto_message *msg
) {
    if (msg->payloadlen) {
        struct json_object *jroot = json_tokener_parse(msg->payload);

        struct json_object *jts;
        struct json_object *jtemp;
        struct json_object *jhum;

        if (
            json_object_object_get_ex(jroot, "timestamp", &jts) &&
            json_object_object_get_ex(jroot, "temperatura", &jtemp) &&
            json_object_object_get_ex(jroot, "humedad", &jhum)
        ) {
            insertar_datos(
                json_object_get_string(jts),
                json_object_get_double(jtemp),
                json_object_get_double(jhum)
            );
        }

        json_object_put(jroot);
    }
}

int main() {
    conn = mysql_init(NULL);

    mysql_real_connect(
        conn,
        "localhost",
        "root",
        "root",
        "sensores",
        0,
        NULL,
        0
    );

    mosquitto_lib_init();

    struct mosquitto *mosq = mosquitto_new(
        "subscriptor_dht",
        false,
        NULL
    );

    mosquitto_message_callback_set(mosq, on_message);

    mosquitto_connect(mosq, BROKER, PORT, 60);

    mosquitto_subscribe(mosq, NULL, TOPIC, MOSQoS);

    mosquitto_loop_forever(mosq, -1, 1);

    mosquitto_destroy(mosq);

    mosquitto_lib_cleanup();

    mysql_close(conn);

    return 0;
}
