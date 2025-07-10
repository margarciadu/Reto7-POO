# Sistema de Pedidos para Restaurante


## Funcionalidades principales

- Gestión de menú (agregar, eliminar, actualizar items).
- Manejo de múltiples pedidos en cola (estructura FIFO).
- Cálculo de totales y descuentos por monto.
- Métodos de pago: tarjeta y efectivo.
- Almacenamiento del menú en archivo JSON.
- Uso de `namedtuple` para combos.

## Estructura del código

- `menu/`: Contiene clases para los items del menú (bebidas, entradas, platos fuertes).
- `restaurant/`: Maneja la cola de pedidos y el procesamiento.
- `data/`: Guarda el archivo `menu.json`.
- `main.py`: Ejecuta el programa con ejemplos de pedidos.
- `combos.py`: Define combos usando `namedtuple`.
