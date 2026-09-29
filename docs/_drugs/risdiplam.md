---
layout: default
title: Risdiplam
parent: Solo Predicción del Modelo (L5)
nav_order: 345
evidence_level: L5
indication_count: 1
---

# Risdiplam
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

# Risdiplam: De Atrofia Muscular Espinal a Acné

## Resumen en Una Frase

Risdiplam es un fármaco de administración oral comercializado en Colombia como EVRYSDI. Los datos del registro no especifican su indicación original. Por conocimiento general, se usa en la atrofia muscular espinal.
El modelo TxGNN predice que podría ser efectivo para **acné**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los datos (el registro solo dice "RISDIPLAM"; la atrofia muscular espinal proviene de conocimiento general) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99.45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 9 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción, y la lista de indicaciones originales está vacía. Por conocimiento general, risdiplam es un modulador del empalme del pre-ARNm de SMN2, usado en la atrofia muscular espinal. Los datos proporcionados no permiten establecer un vínculo mecanístico con el acné.

El acné depende principalmente de la hiperqueratinización folicular, la producción de sebo, la colonización por *Cutibacterium acnes* y la inflamación. Risdiplam no tiene una conexión establecida con ninguna de estas vías.

El puntaje de TxGNN (0.9945) es solo una predicción basada en un grafo de conocimiento y no constituye evidencia clínica. Su base no se puede interpretar con estos datos. El puntaje alto podría deberse a artefactos de la topología del grafo, ya que el fármaco no tiene indicaciones originales ni mecanismo anotados que anclen la predicción. La similitud con la indicación original y la compatibilidad de vías de administración quedan pendientes de evaluar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20197087 | EVRYSDI (F. HOFFMANN - LA ROCHE LTD.) | Polvo para reconstituir a solución oral | Solo aparece el texto "RISDIPLAM" (sin indicación detallada) |

Los datos traen 5 registros idénticos del mismo número sanitario (20197087) y reportan 9 registros en total. Por eso se muestra una sola fila. La única vía de administración registrada es la oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible entre risdiplam y el acné. El puntaje alto de TxGNN no compensa esta falta de respaldo.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones), que actualmente bloquea el tamizaje de seguridad
- Completar el mecanismo de acción desde DrugBank y analizar si existe un vínculo real con la fisiopatología del acné
- Confirmar la indicación original aprobada en Colombia
- Buscar estudios preclínicos o de mecanismo que justifiquen la hipótesis
- Evaluar la compatibilidad de la vía de administración (oral) con las formulaciones habituales para acné
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

