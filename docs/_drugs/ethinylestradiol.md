---
layout: default
title: Ethinylestradiol
parent: Evidencia Moderada (L3-L4)
nav_order: 187
evidence_level: L4
indication_count: 1
---

# Ethinylestradiol
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Etinilestradiol: De Combinación con Dienogest (Registro INVIMA) a Zinc Plasmático Elevado

## Resumen en Una Frase

El etinilestradiol es un estrógeno sintético que en Colombia se comercializa en combinación con dienogest. El registro sanitario no detalla el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **zinc plasmático elevado**, un hallazgo de laboratorio y no una enfermedad establecida.
Hay **0 ensayos clínicos** y **2 publicaciones antiguas e indirectas** (1976 y 1978), que no respaldan un efecto terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dienogest y etinilestradiol (el registro solo indica la composición, no una indicación clínica detallada) |
| Nueva Indicación Predicha | Zinc plasmático elevado |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente curada. Según la información conocida, el etinilestradiol es un estrógeno sintético que actúa sobre los receptores de estrógeno alfa (ESR1) y beta (ESR2). También aparece asociado al transportador de aminoácidos acoplado a protones SLC36A1. Su uso está establecido en anticoncepción combinada, y mecanísticamente podría influir en los niveles de metales traza.

La relación entre la indicación original y la nueva es indirecta. La exposición a estrógenos de los anticonceptivos orales altera los metales circulantes, normalmente elevando el cobre y modificando la distribución del zinc por cambios en proteínas de unión como la ceruloplasmina y la albúmina. Esto es plausible, pero describe un efecto del fármaco sobre un nivel de laboratorio, no el tratamiento de una enfermedad.

Además, los dos estudios recuperados no respaldan claramente la predicción. En mujeres que tomaban anticonceptivos, el cobre subió y el zinc se mantuvo relativamente constante. El otro estudio es en ratas y usó mestranol, un profármaco del etinilestradiol. El puntaje alto de TxGNN (0.996) es una predicción del grafo de conocimiento y ningún ensayo clínico lo corrobora.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [736629](https://pubmed.ncbi.nlm.nih.gov/736629/) | 1978 | Estudio observacional en humanos | Archives of Gynecology | Con cuatro anticonceptivos orales (Ovulen-21, Demulen, Enovid-E, Ovral), el cobre en plasma y endometrio subió de forma significativa. El zinc se mantuvo relativamente constante durante el ciclo menstrual. |
| [961877](https://pubmed.ncbi.nlm.nih.gov/961877/) | 1976 | Estudio preclínico en ratas (aplicabilidad indirecta) | American Journal of Physiology | Ratas hembra con tres niveles de zinc en la dieta recibieron noretindrona, mestranol o ambos. Ambos esteroides redujeron el aumento de peso. El mestranol disminuyó el zinc plasmático y también el cobre tibial y el magnesio. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20093177 | DIENILLE® COMPRIMIDO RECUBIERTOS (EXELTIS S.A.S.) | Tableta recubierta (vía oral) | Dienogest y etinilestradiol |

Nota: el sistema informa 20 registros en total, pero el detalle disponible repite cinco veces el mismo registro (20093177). Por eso se muestra una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No hay advertencias ni contraindicaciones disponibles, y la consulta de interacciones solo devolvió dianas farmacológicas (ESR1, ESR2, SLC36A1), no interacciones entre medicamentos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en dos estudios antiguos e indirectos. Uno de ellos muestra que el zinc no cambió, y el otro es preclínico y con otro compuesto. Además, "zinc plasmático elevado" es un hallazgo de laboratorio y no una indicación terapéutica clara, y el sentido del efecto no está confirmado.

**Para avanzar se necesita:**
- Aclarar si "zinc plasmático elevado" es una condición clínica tratable y qué resultado clínico se buscaría.
- Estudios con etinilestradiol directamente (no mestranol) que confirmen el sentido del efecto sobre el zinc.
- Datos del mecanismo de acción desde una fuente curada (DrugBank).
- Advertencias y contraindicaciones del prospecto INVIMA, necesarias para el tamizaje de seguridad.
- Confirmar la indicación aprobada real de los registros, ya que el texto actual solo indica la composición.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

