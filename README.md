# Módulo de Gestión de Contratos Estudiantiles para Odoo 18

![Banner del Módulo](https://github.com/user-attachments/assets/705789ed-7560-437a-819a-963e7c7b9185)

## Tabla de Contenidos
- [Descripción](#descripción)
- [Características Principales](#características-principales)
- [Instalación](#instalación)
- [Configuración](#configuración-inicial)
- [Uso](#flujo-de-trabajo-principal)
- [Requisitos](#requisitos)

## Descripción
Módulo completo para la gestión de contratos estudiantiles dentro de Odoo ERP, incluyendo:
- Creación y administración de contratos
- Asignación de materias y profesores
- Generación automática de facturas
- Dashboard informativo (vía enlace)

## Características Principales

### 1. Gestión de Estudiantes
![Interfaz Estudiantes](https://github.com/user-attachments/assets/8a30237b-bc3f-40e7-ad15-d86d8d78a099)
- Herencia desde el módulo de Contactos
- Asignación de materias por estudiante
  ![image](https://github.com/user-attachments/assets/fad6db72-6674-49d0-bff6-c7c1f787a1f9)

### 2. Administración de Profesores
![Interfaz Profesores](https://github.com/user-attachments/assets/7a695a8f-d594-4888-a815-3b57c7c0e41f)
- Vinculación con módulo de Empleados
- Asignación de materias a docentes
  ![image](https://github.com/user-attachments/assets/08232abe-0ab3-42b8-a6d7-c4be2adc6130)

### 3. Contratos Estudiantiles
![Interfaz Contratos](https://github.com/user-attachments/assets/16d5dd75-fb48-49a5-8891-e30ca293c2a9)
- Creación de contratos
- Integración con facturación automática
- Gestión de estados y pagos

### 4. Dashboard Informativo
![Vista Dashboard](https://github.com/user-attachments/assets/4a1a3b6b-9c89-4f71-ae7c-36ecd57d2752)
- Visualización de enlace configurado en Odoo
  ![image](https://github.com/user-attachments/assets/9281bf3e-62e2-4d70-8cb8-1d524b8b9591)

## Instalación
1. Copiar el módulo a la carpeta `addons` de Odoo
2. Reiniciar el servidor Odoo
3. Actualizar lista de módulos:
   - Menú **Aplicaciones** → **Actualizar lista de aplicaciones**
4. Buscar e instalar "student_contract", "student_contract_dashboard"

## Configuración Inicial

### 1. Configuración de Materias
![Configuración Materias](https://github.com/user-attachments/assets/17868b7c-51a9-463a-8610-b6d5ed61ed88)
- Vincular cada materia con un producto/servicio
- Establecer valor académico
  
### 2. Configuración de Cursos
![Configuración Cursos](https://github.com/user-attachments/assets/7e4517e4-22fd-40bb-9b56-9673486131b6)
- Crear periodos académicos (trimestres/semestres)
- Asignar materias a cada curso

### 3. Configuración del Dashboard
![Config Dashboard](https://github.com/user-attachments/assets/02cf354f-1250-44f6-9a79-9d19a9a85c2b)
- Ingresar URL del dashboard
- Asignar permisos a usuarios

## Flujo de Trabajo Principal

1. **Configurar Profesores**:
   - Materias → Cursos → Profesores
2. **Registrar estudiantes**:
   - Asignar materias por curso
3. **Generar contratos**:
   - Validar y confirmar
   - Validar → Factura automática → Confirmar Factura
   - Adjuntar Pago (proceso nativo de Odoo)

## Requisitos
- Odoo 18.0+
- Módulos dependientes:
  - `hr`
  - `account`
  - `product`

*© 2025 - Todos los derechos reservados*
