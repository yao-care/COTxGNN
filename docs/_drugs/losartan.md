---
layout: default
title: Losartan
parent: Evidencia Moderada (L3-L4)
nav_order: 265
evidence_level: L4
indication_count: 8
---

# Losartan
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **8** 
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

# Losartán: De Antihipertensivo (ARA II) a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Losartán es un antagonista del receptor de angiotensina II tipo 1 (AT1), conocido como antihipertensivo. En Colombia se comercializa sola y combinada con un diurético.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna**,
pero hoy solo hay **0 ensayos clínicos** y **1 publicación preclínica** (modelo animal) que apunten en esa dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo indica "LOSARTAN" (sin texto de indicación). Uso conocido: antagonista del receptor AT1 |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, losartán es un bloqueador del receptor AT1 de la angiotensina II. Como antihipertensivo, su eficacia para controlar la presión arterial es conocida, y mecanísticamente podría ser aplicable a la enfermedad renal hipertensiva maligna.

La enfermedad renal hipertensiva maligna (nefroesclerosis hipertensiva maligna) es el daño renal grave que produce una hipertensión muy severa. El único artículo de apoyo (PMID 30809002) describe, en un modelo de rata, que la angiotensina II y la vía NF-κB participan en el daño renal de este cuadro. Bloquear el receptor AT1 encaja con ese mecanismo.

Este respaldo es indirecto. El estudio es preclínico, no prueba losartán en pacientes y, según los datos disponibles, tampoco confirma que se haya evaluado losartán. El vínculo se basa en la farmacología general de los ARA II.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30809002](https://pubmed.ncbi.nlm.nih.gov/30809002/) | 2019 | Preclínico (modelo animal) | Hypertension Research | En ratas con modelo de nefroesclerosis hipertensiva maligna (uninefrectomía y sobrecarga de sal), se estudia el papel de la angiotensina II y del sistema NF-κB en el daño renal |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20189581 | SANTANIL® 50 mg | Tableta recubierta | Losartán (el registro no detalla la indicación) |
| 20263318 | LOSAN HCT® | Tableta recubierta | Losartán y diuréticos (el registro no detalla la indicación) |

Nota: el total declarado es de 6 registros, pero los datos entregados solo muestran 2 números de registro distintos (con filas repetidas).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.73%), pero solo la respalda un estudio preclínico indirecto (L4), sin ensayos clínicos. Además, faltan los datos de seguridad del prospecto de INVIMA, que bloquean el paso al cribado de seguridad. En el estado actual es una pregunta de investigación, no una candidata para avanzar.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es el vacío bloqueante.
- Obtener el mecanismo de acción desde DrugBank.
- Confirmar si el estudio PMID 30809002 evaluó losartán o un bloqueador del sistema renina-angiotensina.
- Buscar evidencia clínica (ensayos o estudios observacionales) en enfermedad renal hipertensiva maligna.
- Definir el criterio de seguridad renal, ya que la estenosis de la arteria renal es una precaución conocida de los ARA II.

**Otras predicciones del modelo:** la hipertensión renovascular maligna (L4) tiene solo un reporte de caso y un artículo de métodos en ratas. La enfermedad de pequeño vaso cerebral (L4) tiene un ensayo cruzado con antihipertensivos (PMID 37863608) cuyo diseño y uso de losartán no se pueden confirmar con los datos entregados. Las demás predicciones (hipertensión pulmonar, síndrome de Braddock, angina de Prinzmetal y síndrome familiar de hematuria con tortuosidad arteriolar retiniana) son L5, sin evidencia real, y quedan en Hold.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

