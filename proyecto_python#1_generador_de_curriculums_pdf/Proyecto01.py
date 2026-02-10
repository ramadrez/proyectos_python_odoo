"""
Generador de Currículum en PDF
Este programa solicita información personal y profesional al usuario
y genera un currículum vitae en formato PDF.
"""

from fpdf import FPDF

# ============================================================================
# CONSTANTES DE CONFIGURACIÓN
# ============================================================================

# Archivo de salida
NOMBRE_ARCHIVO_PDF = "Curriculum.pdf"
IMAGEN_PLANTILLA = "image.png"

# Fuentes
FUENTE_PRINCIPAL = "Arial"
TAMAÑO_FUENTE_NOMBRE = 30
TAMAÑO_FUENTE_TITULO = 12
TAMAÑO_FUENTE_CONTACTO = 9
TAMAÑO_FUENTE_SUBTITULO = 11
TAMAÑO_FUENTE_TEXTO = 9

# Posiciones (no modificar - alineadas con la imagen de plantilla)
POS_NOMBRE_X, POS_NOMBRE_Y = 20, 35
POS_TITULO_X, POS_TITULO_Y = 20, 42
POS_CONTACTO_X = 130
POS_TELEFONO_Y = 31.5
POS_CORREO_Y = 38.3
POS_DIRECCION_Y = 46
POS_SOBRE_MI_X, POS_SOBRE_MI_Y = 60, 68
POS_HABILIDADES_X, POS_HABILIDADES_Y = 60, 105
POS_TRABAJO1_X, POS_TRABAJO1_Y = 60, 140
POS_TAREAS1_Y = 148
POS_TRABAJO2_X, POS_TRABAJO2_Y = 60, 175
POS_TAREAS2_Y = 183
POS_EDUCACION_X, POS_EDUCACION_Y = 60, 215
POS_TITULO_EDUCACION_Y = 225

# Dimensiones
ANCHO_CONTENIDO = 140
ALTURA_LINEA_TEXTO = 4
ALTURA_LINEA_LISTA = 6


# ============================================================================
# RECOPILACIÓN DE INFORMACIÓN PERSONAL
# ============================================================================

print("=" * 60)
print("GENERADOR DE CURRÍCULUM VITAE")
print("=" * 60)
print("\n--- INFORMACIÓN PERSONAL ---")

nombre_completo = input("Ingrese su nombre completo: ")
titulo_profesional = input("Ingrese su título o profesión: ")
numero_telefono = input("Ingrese su número de teléfono (sin el símbolo +): ")
telefono_formateado = f"+{numero_telefono}"
correo_electronico = input("Ingrese su correo electrónico: ")
direccion_completa = input("Ingrese su dirección: ")

print("\n--- PERFIL PROFESIONAL ---")
descripcion_personal = input("Escriba una breve descripción sobre usted (perfil profesional): ")

print("\n--- HABILIDADES ---")
print("Ingrese sus principales habilidades:")
habilidad_1 = input("  Habilidad #1: ")
habilidad_2 = input("  Habilidad #2: ")
habilidad_3 = input("  Habilidad #3: ")
habilidad_4 = input("  Habilidad #4: ")

print("\n--- EXPERIENCIA LABORAL ---")
print("Trabajo más reciente:")
titulo_trabajo_reciente = input("  Título del puesto: ")
tarea_reciente_1 = input("  Responsabilidad #1: ")
tarea_reciente_2 = input("  Responsabilidad #2: ")
tarea_reciente_3 = input("  Responsabilidad #3: ")

print("\nTrabajo anterior:")
titulo_trabajo_anterior = input("  Título del puesto: ")
tarea_anterior_1 = input("  Responsabilidad #1: ")
tarea_anterior_2 = input("  Responsabilidad #2: ")
tarea_anterior_3 = input("  Responsabilidad #3: ")

print("\n--- EDUCACIÓN ---")
nombre_institucion = input("Ingrese el nombre de la institución educativa: ")
titulo_academico = input("Ingrese el título académico obtenido: ")

print("\n" + "=" * 60)
print("Generando su currículum en PDF...")
print("=" * 60)


# ============================================================================
# GENERACIÓN DEL PDF
# ============================================================================

# Inicializar documento PDF
pdf = FPDF()
pdf.add_page()

# Insertar imagen de plantilla de fondo
pdf.image(IMAGEN_PLANTILLA, 0, 0, pdf.w)


# --- SECCIÓN: ENCABEZADO (Nombre y Título) ---
pdf.set_font(FUENTE_PRINCIPAL, size=TAMAÑO_FUENTE_NOMBRE, style="B")
pdf.text(POS_NOMBRE_X, POS_NOMBRE_Y, nombre_completo)

pdf.set_font(FUENTE_PRINCIPAL, size=TAMAÑO_FUENTE_TITULO)
pdf.text(POS_TITULO_X, POS_TITULO_Y, titulo_profesional)


# --- SECCIÓN: INFORMACIÓN DE CONTACTO ---
pdf.set_font(FUENTE_PRINCIPAL, size=TAMAÑO_FUENTE_CONTACTO)
pdf.text(POS_CONTACTO_X, POS_TELEFONO_Y, telefono_formateado)
pdf.text(POS_CONTACTO_X, POS_CORREO_Y, correo_electronico)
pdf.text(POS_CONTACTO_X, POS_DIRECCION_Y, direccion_completa)


# --- SECCIÓN: SOBRE MÍ ---
pdf.set_xy(POS_SOBRE_MI_X, POS_SOBRE_MI_Y)
pdf.multi_cell(ANCHO_CONTENIDO, ALTURA_LINEA_TEXTO, descripcion_personal, align="J")


# --- SECCIÓN: HABILIDADES ---
lista_habilidades = [habilidad_1, habilidad_2, habilidad_3, habilidad_4]
pdf.set_xy(POS_HABILIDADES_X, POS_HABILIDADES_Y)
for habilidad in lista_habilidades:
    pdf.multi_cell(ANCHO_CONTENIDO, ALTURA_LINEA_LISTA, f"- {habilidad}", align="L")
    pdf.set_x(POS_HABILIDADES_X)


# --- SECCIÓN: EXPERIENCIA LABORAL ---

# Trabajo más reciente
pdf.set_font(FUENTE_PRINCIPAL, size=TAMAÑO_FUENTE_SUBTITULO, style="B")
pdf.set_xy(POS_TRABAJO1_X, POS_TRABAJO1_Y)
pdf.multi_cell(ANCHO_CONTENIDO, ALTURA_LINEA_TEXTO, titulo_trabajo_reciente, align="J")

pdf.set_font(FUENTE_PRINCIPAL, size=TAMAÑO_FUENTE_TEXTO)
lista_tareas_recientes = [tarea_reciente_1, tarea_reciente_2, tarea_reciente_3]
pdf.set_xy(POS_TRABAJO1_X, POS_TAREAS1_Y)
for tarea in lista_tareas_recientes:
    pdf.multi_cell(ANCHO_CONTENIDO, ALTURA_LINEA_LISTA, f"- {tarea}", align="L")
    pdf.set_x(POS_TRABAJO1_X)

# Trabajo anterior
pdf.set_font(FUENTE_PRINCIPAL, size=TAMAÑO_FUENTE_SUBTITULO, style="B")
pdf.set_xy(POS_TRABAJO2_X, POS_TRABAJO2_Y)
pdf.multi_cell(ANCHO_CONTENIDO, ALTURA_LINEA_TEXTO, titulo_trabajo_anterior, align="J")

pdf.set_font(FUENTE_PRINCIPAL, size=TAMAÑO_FUENTE_TEXTO)
lista_tareas_anteriores = [tarea_anterior_1, tarea_anterior_2, tarea_anterior_3]
pdf.set_xy(POS_TRABAJO2_X, POS_TAREAS2_Y)
for tarea in lista_tareas_anteriores:
    pdf.multi_cell(ANCHO_CONTENIDO, ALTURA_LINEA_LISTA, f"- {tarea}", align="L")
    pdf.set_x(POS_TRABAJO2_X)


# --- SECCIÓN: EDUCACIÓN ---
pdf.set_font(FUENTE_PRINCIPAL, size=TAMAÑO_FUENTE_SUBTITULO, style="B")
pdf.set_xy(POS_EDUCACION_X, POS_EDUCACION_Y)
pdf.multi_cell(ANCHO_CONTENIDO, ALTURA_LINEA_TEXTO, nombre_institucion, align="J")

pdf.set_font(FUENTE_PRINCIPAL, size=TAMAÑO_FUENTE_TEXTO, style="B")
pdf.set_xy(POS_EDUCACION_X, POS_TITULO_EDUCACION_Y)
pdf.multi_cell(ANCHO_CONTENIDO, ALTURA_LINEA_TEXTO, titulo_academico, align="J")


# --- GUARDAR ARCHIVO PDF ---
pdf.output(NOMBRE_ARCHIVO_PDF)

print(f"\n✓ Currículum generado exitosamente: {NOMBRE_ARCHIVO_PDF}")
