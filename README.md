# VFY - Programming Exercises Verification Tool

VFY es una herramienta para practicar ejercicios de programación en C con verificación automática.

## Características

- **Ejercicios organizados por niveles** de dificultad
- **Verificación automática** de tus soluciones
- **Plantillas de código** para empezar rápidamente
- **Interfaz amigable** con colores y formato agradable
- **Personalizable** a través de configuraciones
- **Creación de ejercicios** para profesores o usuarios que quieran contribuir

## Instalación

### Usando pip (recomendado)

La forma más fácil de instalar VFY es usando pip:

```bash
# Instalar directamente desde GitHub
pip install git+https://github.com/tu-usuario/vfy.git

# O desde el directorio local
git clone https://github.com/tu-usuario/vfy.git
cd vfy
pip install -e .
```

### Instalación para un solo usuario (alternativa)

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/vfy.git
cd vfy

# Instalar para el usuario actual (no requiere sudo)
make user-install

# Añadir al PATH (añade esta línea a tu .bashrc o .zshrc)
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Instalación a nivel de sistema

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/vfy.git
cd vfy

# Instalar a nivel de sistema (requiere sudo)
sudo make install
```

## Uso básico

```bash
# Ver ayuda
vfy help

# Listar niveles disponibles
vfy list

# Listar ejercicios en el nivel 1
vfy list 1

# Obtener un ejercicio aleatorio del nivel 1
vfy get 1

# Editar la solución del ejercicio actual
vfy edit

# Comprobar la solución
vfy check

# Ver el estado del ejercicio actual
vfy status
```

## Personalización

Puedes configurar varias opciones:

```bash
# Ver configuración actual
vfy config

# Cambiar ubicación de los ejercicios
vfy config exercises_dir ~/mis_ejercicios

# Cambiar editor por defecto
vfy config editor nano

# Activar/desactivar apertura automática del editor
vfy config auto_open_editor false

# Añadir flags del compilador
vfy config compiler_flags "-Wall -Wextra -Werror"
```

También puedes usar variables de entorno:

```bash
# Definir ubicación de los ejercicios
export VFY_EXERCISES_DIR=~/mis_ejercicios

# Definir ubicación de los sujetos
export VFY_SUBJECTS_DIR=~/mis_ejercicios_sujetos

# Definir compilador
export CC=gcc
```

## Creación de ejercicios

Puedes crear tus propios ejercicios:

```bash
vfy create
```

O crear ejercicios manualmente:

1. Crea un directorio en `~/.vfy/subjects/level_X/nombre_ejercicio`
2. Añade los siguientes archivos:
   - `subject.txt`: Descripción del ejercicio
   - `expected_output.txt`: Salida esperada del programa
   - `template.c`: Plantilla de código para el usuario

## Desinstalación

```bash
# Desinstalar (con sudo si usaste instalación a nivel de sistema)
sudo make uninstall
```

## Contribución

Si quieres contribuir a este proyecto:

1. Haz un fork del repositorio
2. Crea una rama (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -am 'Añade nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request 