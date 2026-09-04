| Servicio            | Descripcion  |
|---------------------|-----------|
| /register           | Dato 1    |
| /profile/{id}       | Dato 2    |
| /provider/setup 3   | Dato 3    |
| /providers/search   | Filtrar proveedores por category_id, rating_avg o ubicación.          |

POST /register: Crear un nuevo usuario en la tabla users.
GET /profile/{id}: Obtener datos básicos del usuario.
POST /provider/setup: Si el usuario quiere ofrecer servicios, crea su entrada en provider_profiles y vincula sus categories (ej. Plomería, Electricidad) en la tabla provider_categories.
GET /providers/search: Filtrar proveedores por category_id, rating_avg o ubicación.