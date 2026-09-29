---
layout: default
title: Turoctocog Alfa Pegol
parent: Solo Predicción del Modelo (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa Pegol
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

# Turoctocog alfa pegol: De Coagulación (Factor VIII) a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Turoctocog alfa pegol es un factor VIII de coagulación recombinante pegilado, comercializado en Colombia como ESPEROCT® y registrado para la coagulación por factor VIII.
El modelo TxGNN predice que podría ser efectivo para **trastorno primario de liberación plaquetaria**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Coagulación factores VIII |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Turoctocog alfa pegol es un factor VIII recombinante pegilado. El factor VIII actúa como cofactor del factor IXa en el complejo tenasa, que impulsa la cascada de coagulación. Actualmente no se dispone de datos detallados del mecanismo de acción en las fuentes consultadas; la descripción anterior proviene de la clase del fármaco.

Los trastornos de liberación (secreción) plaquetaria son defectos intrínsecos de la plaqueta. Reponer factor VIII no corregiría ese defecto, por lo que no se identifica un mecanismo directo que conecte el fármaco con esta enfermedad. El puntaje alto de TxGNN proviene de relaciones en el grafo de conocimiento, no de evidencia clínica.

Las demás predicciones del top 10 siguen el mismo patrón. La mayoría son defectos plaquetarios (pseudo-enfermedad de von Willebrand, trombastenia de Glanzmann, síndrome de Scott, defecto del receptor de colágeno, trombocitopenias constitucionales y aloinmune), y el factor VIII no actúa sobre ellos. La única con plausibilidad mecanística es la **deficiencia adquirida de factores de coagulación** (puntaje 99.974%), que se considera solo una pregunta de investigación. Es una categoría muy amplia, y en la hemofilia A adquirida los autoanticuerpos inhibidores neutralizarían el producto. Además, el término "flood factor deficiency" no es claro y podría ser un artefacto de mapeo de la ontología.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Se reportan 20 registros sanitarios. Los 5 registros del listado son idénticos (mismo número de registro, mismo producto), por lo que se presentan en una sola fila.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20189841 | ESPEROCT® 1000UI (Novo Nordisk A/S) | Polvo estéril para reconstituir a solución inyectable | Coagulación factores VIII |

También existe una presentación en polvo liofilizado para reconstituir a solución inyectable.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas para este fármaco.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni literatura (nivel L5). Además, no existe un mecanismo plausible que conecte el factor VIII con los defectos plaquetarios predichos.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) y de la indicación original desde DrugBank
- Prospecto de INVIMA con advertencias y contraindicaciones
- Definir el subtipo concreto de "deficiencia adquirida de factores de coagulación", el único candidato mecanísticamente plausible, y revisar la literatura antes de reconsiderarlo
- Verificar el término "flood factor deficiency" contra la ontología de origen
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

