---
layout: default
title: Glimepiride
parent: Solo Predicción del Modelo (L5)
nav_order: 210
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Glimepirida: De Metformina y Sulfonilureas a Síndrome de Extremidad Rígida Focal

## Resumen en Una Frase

Glimepirida es una sulfonilurea, y en Colombia está registrada en una combinación con metformina para el tratamiento de la diabetes.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de extremidad rígida focal**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Metformina y sulfonilureas (texto del registro sanitario) |
| Nueva Indicación Predicha | Síndrome de extremidad rígida focal |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la glimepirida es una sulfonilurea que cierra los canales de potasio sensibles a ATP (K-ATP) de las células beta del páncreas y estimula la secreción de insulina. Su eficacia se ha comprobado en diabetes, pero no en trastornos neurológicos.

El síndrome de extremidad rígida focal pertenece al espectro de los síndromes de rigidez, que son trastornos autoinmunes o de inhibición neuronal (anticuerpos anti-GAD65 o antianfifisina, y alteración de la señalización GABAérgica). No se ha establecido un vínculo mecanístico con la glimepirida.

La única conexión plausible es la coexistencia frecuente de autoinmunidad y diabetes. Eso no constituye una justificación terapéutica. El puntaje alto de TxGNN (0.997) parece reflejar una señal de vecindad en el grafo de conocimiento, no un efecto del tratamiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Se recibieron 5 filas de registros, todas con el mismo número de registro sanitario, por lo que se presentan una sola vez. El total reportado es de 20 registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20046981 | METGLITAL LEX 850/4 MG (tabletas de liberación prolongada), Laboratorios Silanes S.A. de C.V. | Tableta de liberación prolongada (vía oral) | Metformina y sulfonilureas |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura que respalden el síndrome de extremidad rígida focal (nivel L5), y no existe un mecanismo plausible que explique un efecto de la glimepirida. El puntaje alto de TxGNN parece un artefacto del grafo. Las otras ocho predicciones evaluadas (síndrome de persona rígida clásico, opsismodisplasia, distintas lipodistrofias localizadas, agenesia pancreática, entre otras) también quedan en Hold, todas con nivel L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la glimepirida, para analizar el vínculo mecanístico.
- Advertencias y contraindicaciones del prospecto de INVIMA, necesarias para el tamizaje de seguridad.
- Evidencia real (ensayos, series de casos o estudios preclínicos) que conecte la glimepirida con los síndromes de rigidez.
- Una revisión clínica que confirme si la señal proviene solo de la comorbilidad con diabetes autoinmune.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

