---
layout: default
title: Salbutamol
parent: Solo Predicción del Modelo (L5)
nav_order: 354
evidence_level: L5
indication_count: 10
---

# Salbutamol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Salbutamol: De Asma y EPOC (uso clínico conocido) a Conjuntivitis Papilar

## Resumen en Una Frase

Salbutamol es un agonista selectivo del receptor β2-adrenérgico, usado como broncodilatador en asma y EPOC. Se comercializa en Colombia en forma de aerosol.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis papilar**, pero hoy hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo repite "SALBUTAMOL" como texto de indicación, sin describir un uso clínico. Por la base farmacológica consultada, el uso conocido es asma y EPOC |
| Nueva Indicación Predicha | Conjuntivitis papilar |
| Puntaje de Predicción TxGNN | 99,996 % (posición 87 en el ranking del modelo) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la base farmacológica consultada, salbutamol es un agonista altamente selectivo del receptor β2-adrenérgico (gen ADRB2). Su eficacia en obstrucción reversible de las vías aéreas está comprobada, y mecanísticamente podría ser aplicable a enfermedad alérgica ocular.

La relación con la conjuntivitis papilar es indirecta. Un agonista β2 podría reducir la liberación de mediadores de los mastocitos, que participan en la inflamación alérgica ocular. Ese es el único argumento a favor, y es una hipótesis.

No hay estudios que la respalden, y la relación no está establecida para la conjuntivitis papilar en concreto. La única presentación comercializada en Colombia es un aerosol inhalado, así que la compatibilidad de vía de administración con el uso ocular sigue sin evaluarse.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19992498 | SACRUSYT® (FAES FARMA COLOMBIA S.A.S.) | Aerosoles | SALBUTAMOL (el texto no describe una indicación clínica) |

Los datos traen cinco entradas idénticas, todas con el mismo número de registro, aunque el total declarado es 6. Parecen duplicados y conviene depurarlos en la fuente.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ningún respaldo en ensayos ni literatura (nivel L5), y el argumento mecanístico es general. Además, faltan los datos de seguridad del prospecto de INVIMA, que bloquean el cribado de seguridad.

Otras indicaciones predichas para salbutamol tienen más respaldo que esta. Bronquitis y anafilaxia están en L3, con ensayos y literatura directos. Conjuntivitis atópica tiene evidencia preclínica, incluida una en cobayos con salbutamol tópico. Obstrucción pulmonar es probablemente un uso ya establecido. Si se busca una línea de reposicionamiento, conviene priorizar esas.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones)
- Completar el mecanismo de acción desde DrugBank
- Corregir el campo de indicaciones originales, que hoy solo dice "SALBUTAMOL"
- Hacer una búsqueda dirigida sobre agonistas β2 en conjuntivitis alérgica y papilar
- Evaluar si el uso ocular requeriría una formulación o vía distinta al aerosol inhalado actual
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

