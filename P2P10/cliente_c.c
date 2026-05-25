#include <stdio.h>
#include <mosquitto.h>

void mensaje_callback(struct mosquitto *mosq, void *userdata, const struct mosquitto_message *msg) {
    printf("Mensaje recibido en tópico '%s': %s\n",
           msg->topic,
           (char *)msg->payload);
}

int main() {
    mosquitto_lib_init();

    struct mosquitto *mosq = mosquitto_new("ClienteC", true, NULL);

    if (!mosq) {
        fprintf(stderr, "Error al crear el cliente.\n");
        return 1;
    }

    mosquitto_message_callback_set(mosq, mensaje_callback);

    mosquitto_connect(mosq, "localhost", 1883, 60);
    mosquitto_subscribe(mosq, NULL, "iot/temperatura", 0);

    mosquitto_loop_forever(mosq, -1, 1);

    mosquitto_destroy(mosq);
    mosquitto_lib_cleanup();

    return 0;
}

