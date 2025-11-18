# 🏗 Dosificación Automática de Concreto (ACI)

## 📘 Descripción General

Este proyecto implementa un programa en Python con Tkinter que realiza la dosificación automática de concreto siguiendo las recomendaciones del ACI (American Concrete Institute).

El objetivo es calcular la cantidad de cemento, arena, grava y agua necesarios para un volumen específico de concreto, considerando la resistencia deseada (f'c) y el tamaño máximo del agregado. El sistema incluye una interfaz gráfica intuitiva que permite al usuario ingresar los datos y visualizar los resultados en una tabla clara y organizada.

---
 
## ⚙ Funcionalidades

Ingreso de los datos de entrada:

Resistencia deseada del concreto f'c (kg/cm²)

Volumen total de concreto (m³)

Tamaño máximo del agregado (mm) (opciones: 20, 40, 80)

Validación automática de los valores ingresados:

f'c mínimo permitido: 150 kg/cm²

f'c máximo permitido: 400 kg/cm²

Cálculo de la relación Agua/Cemento según la tabla ACI.

Determinación de la cantidad de cada material (cemento, arena, grava, agua) por m³ y total para el volumen indicado.

Visualización de resultados en una tabla interactiva.

Resumen de los parámetros utilizados y la dosificación calculada.

Mensajes de advertencia si los valores ingresados no cumplen criterios de diseño.

---

## 🧮 Fundamento Teórico

La dosificación se basa en las tablas de ACI y en la relación agua/cemento según la resistencia deseada:

Tabla ACI: Relación Agua/Cemento según f'c (kg/cm²)
| f'c (kg/cm²) | Relación A/C |
| ------------ | ------------ |
| 150          | 0.70         |
| 200          | 0.60         |
| 250          | 0.55         |
| 300          | 0.50         |
| 350          | 0.45         |
| 400          | 0.40         |


La relación Agua/Cemento (A/C) se selecciona según la resistencia deseada. Por ejemplo, si se solicita f'c = 250 kg/cm², la relación A/C será 0.55.

Tabla de Agua según tamaño máximo del agregado
| Tamaño agregado (mm) | Agua (kg/m³) |
| -------------------- | ------------ |
| 20                   | 205          |
| 40                   | 185          |
| 80                   | 170          |


A partir de estas tablas se calcula:

Cemento (kg/m³) = Agua (kg/m³) / Relación A/C

Las proporciones típicas de materiales ACI (cemento : arena : grava) = 1 : 1.5 : 2.5, que se multiplican por los pesos específicos para obtener las cantidades de arena y grava por m³.

---

## 🧰 Tecnologías Utilizadas

Python 3.8+

Tkinter: Interfaz gráfica

Numpy: Cálculos numéricos

---

## 🖥 Interfaz Gráfica
### 💡 Características Visuales

Ventana con estilo profesional y moderno (tema "clam")

Panel de entrada de datos con etiquetas claras y campos guiados

Tabla de resultados con tipografía legible y filas de altura adecuada

Resumen de cálculo mostrado al final


---

## 🧩 Componentes principales
| Sección             | Descripción                                                                        |
| ------------------- | ---------------------------------------------------------------------------------- |
| Entrada de datos    | Campos para f'c, volumen y tamaño máximo de agregado                               |
| Botón "Calcular"    | Ejecuta la dosificación automática                                                 |
| Tabla de resultados | Muestra la cantidad de cada material: cemento, arena, grava y agua, por m³ y total |
| Resumen             | Muestra f'c ingresado, relación A/C, tamaño agregado y volumen                     |

