sequenceDiagram
    participant U as Usuario
    participant A as Aplicación
    participant C as Conductor
    participant P as Sistema de Pago

    U->>A: Solicita un viaje
    A->>A: Busca conductores cercanos
    A->>C: Notifica nueva solicitud de viaje
    C->>A: Acepta el viaje
    A->>U: Confirma viaje y muestra detalles del conductor
    U->>A: Confirma ubicación de recogida
    A->>C: Envía ubicación de recogida
    C->>U: Llega al punto de recogida
    U->>C: Sube al vehículo
    C->>A: Inicia el viaje
    C->>A: Finaliza el viaje
    A->>P: Procesa el pago
    P->>A: Confirma pago exitoso
    A->>U: Solicita calificación del viaje
    U->>A: Envía calificación y comentarios
    A->>C: Actualiza calificación del conductor