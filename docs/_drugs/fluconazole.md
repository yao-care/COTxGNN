---
layout: default
title: Fluconazole
parent: Solo Predicción del Modelo (L5)
nav_order: 201
evidence_level: L5
indication_count: 1
---

# Fluconazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Fluconazol: De Antifúngico Azólico a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

Fluconazol es un antifúngico azólico comercializado en Colombia en cápsulas. El registro sanitario local no detalla su indicación aprobada; solo repite el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para la **queratoconjuntivitis epitelial punteada**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice "Fluconazol") |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.24% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de entrada. Por conocimiento farmacológico general (no respaldado por el registro), el fluconazol inhibe la enzima fúngica CYP51 (lanosterol 14-alfa-desmetilasa), lo que altera la membrana celular del hongo.

La queratoconjuntivitis epitelial punteada suele tener origen viral (sobre todo adenovirus), inflamatorio o tóxico. Un mecanismo antifúngico solo sería plausible si la causa fuera fúngica, y los datos no lo indican. Por eso, hoy **no hay un vínculo mecanístico establecido** entre la indicación original y la nueva.

El puntaje de 0.992 proviene de un grafo de conocimiento y no muestra qué ruta del grafo generó la predicción. No puede tomarse como respaldo mecanístico. La compatibilidad de la vía de administración tampoco está evaluada: el producto registrado es una cápsula dura de uso oral, y no se verificó si existe una presentación oftálmica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20053245 | HONGIZOL® CAPSULAS (MED LINE COLOMBIA S.A.S.) | Cápsula dura | FLUCONAZOL |

Los datos traen cinco entradas idénticas del mismo registro (20053245), que aquí se muestran una sola vez. El total reportado es de 20 registros sanitarios.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (L5), sin ensayos ni publicaciones, y no hay vínculo mecanístico claro con una indicación de origen mayormente viral o inflamatorio. Además, faltan los datos de seguridad locales.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones)
- Obtener el mecanismo de acción desde DrugBank
- Buscar literatura y ensayos que relacionen fluconazol con queratoconjuntivitis epitelial punteada, y confirmar si existe una etiología fúngica que lo justifique
- Evaluar la compatibilidad de la vía de administración (la presentación registrada es oral)
- Aclarar la indicación aprobada real del registro 20053245
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

