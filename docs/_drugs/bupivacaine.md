---
layout: default
title: Bupivacaine
parent: Solo Predicción del Modelo (L5)
nav_order: 101
evidence_level: L5
indication_count: 4
---

# Bupivacaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Bupivacaína: De Anestesia Local a Acrodermatitis Crónica Atrófica

## Resumen en Una Frase

La bupivacaína es un anestésico local que se usa para bloqueos nerviosos y para el dolor posoperatorio.
El modelo TxGNN predice que podría ser efectiva para **acrodermatitis crónica atrófica**,
pero hoy hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. La predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo dice "BUPIVACAINA" y no detalla la indicación. Uso conocido: anestesia local |
| Nueva Indicación Predicha | Acrodermatitis crónica atrófica |
| Puntaje de Predicción TxGNN | 99.23% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la bupivacaína es un anestésico local que bloquea los canales de sodio dependientes de voltaje. Su eficacia como anestésico está comprobada, pero mecanísticamente no hay un puente claro hacia esta nueva indicación.

La acrodermatitis crónica atrófica es una manifestación cutánea tardía de la infección por *Borrelia* y se trata con antibióticos. Nada en la evidencia disponible conecta el bloqueo de canales de sodio con esta enfermedad. El puntaje alto (0.992) es solo una predicción computacional y probablemente sea un artefacto del grafo de conocimiento.

Las cuatro indicaciones predichas son fenotipos muy parecidos: dermatomiositis en sus variantes, enfermedad pulmonar intersticial asociada a enfermedad del tejido conectivo y esta afección cutánea. Es probable que compartan el mismo vecindario del grafo y no sean señales independientes, lo que debilita aún más la predicción.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los datos entregan 5 filas idénticas del mismo registro, por lo que se muestra una sola.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20013329 | BUPINEST 0.75% PESADO (ROPSOHN THERAPEUTICS S.A.S.) | Solución inyectable | BUPIVACAINA (sin detalle de indicación) |

## Consideraciones de Seguridad

- **Interacciones farmacológicas (farmacología de dianas)**: la consulta se completó con 4 registros. Son dianas moleculares de la bupivacaína, no interacciones con otros medicamentos:
  - Nav1.5 (SCN5A, humano): canal de sodio cardíaco
  - Kv1.5 (KCNA5, humano)
  - Kv4.3 (Kcnd3, ratón)
  - Kir3.2
- Las fuentes no aportan datos de afinidad para confirmar el mecanismo sobre canales de sodio humanos.
- **Preocupaciones teóricas** para las indicaciones predichas: la bupivacaína es miotóxica a concentraciones locales altas, lo que preocupa en una enfermedad muscular inflamatoria como la dermatomiositis. El uso neonatal añade otra preocupación.

Consultar el prospecto para información completa de advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las cuatro predicciones son nivel L5, sin ensayos ni publicaciones, y no hay vínculo mecanístico plausible. Además, existen preocupaciones teóricas de seguridad (miotoxicidad, uso neonatal).

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones)
- Obtener datos de mecanismo de acción desde DrugBank
- Estudios preclínicos o clínicos que muestren alguna relación entre la bupivacaína y la enfermedad predicha
- Aclarar la indicación aprobada en los registros, que hoy solo repiten el nombre del principio activo

> Este resultado es solo para investigación y no constituye consejo médico. Todo candidato de reposicionamiento requiere validación clínica antes de aplicarse.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

