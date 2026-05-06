# 🛒 Ecommerce Backend API - FastAPI

API REST completa para un sistema ecommerce desarrollada con FastAPI, SQLAlchemy y MySQL.

Incluye autenticación con JWT, control de roles, gestión de productos, carrito de compras y flujo completo de pedidos.

---

## 🚀 Tecnologías

- FastAPI
- Python
- SQLAlchemy (ORM)
- MySQL
- JWT Authentication
- Pydantic

---

## 🧠 Funcionalidades

### 🔐 Autenticación
- Registro de usuarios
- Login con JWT
- Control de acceso por roles (Admin, Proveedor, Cliente)

### 📦 Productos
- CRUD completo
- Permisos por rol
- Catálogo público con filtros, búsqueda y paginación

### 🛒 Carrito
- Agregar productos
- Modificar cantidades
- Eliminar productos
- Cálculo dinámico del total

### 📑 Pedidos
- Crear pedido desde carrito
- Validación de stock
- Persistencia de pedido e items
- Historial de pedidos
- Detalle de pedido
- Cancelación con reglas de negocio

---

## 📁 Estructura del proyecto

app/
│── api/ # Endpoints
│── models/ # Modelos SQLAlchemy
│── schemas/ # Validaciones Pydantic
│── services/ # Lógica de negocio
│── db/ # Conexión DB
│── core/ # Configuración

## ⚙️ Instalación

```bash
git clone https://github.com/Nezareth07/ecommerce.git
cd ecommerce

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
uvicorn main:app --reload

```markdown

📖 Documentación

Accede a la documentación automática:

http://localhost:8000/docs

📌 Estado del proyecto

✅ Autenticación
✅ Productos
✅ Carrito
✅ Pedidos

🚧 Próximamente:

Pagos (Stripe / MercadoPago)
Integración WhatsApp
Deploy

🧠 Arquitectura

El proyecto sigue una arquitectura modular por capas:

Router → Service → Model → Database

Separando responsabilidades para facilitar escalabilidad y mantenimiento.

👨‍💻 Autor

Nezareth Niño
📧 nezavirg159@gmail.com