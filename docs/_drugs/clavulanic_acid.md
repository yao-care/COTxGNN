---
layout: default
title: Clavulanic Acid
parent: Solo Predicción del Modelo (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Clavulanic Acid: nueva indicación predicha, Uretritis por Ureaplasma (nivel de evidencia L5). Indicación original: Amoxicilina y inhibidor de betalactamasa"
---

# Clavulanic Acid
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

# Ácido clavulánico: De Amoxicilina con Inhibidor de Betalactamasa a Uretritis por Ureaplasma

## Resumen en Una Frase

El ácido clavulánico es un inhibidor de betalactamasas que se usa combinado con amoxicilina como antibacteriano. El modelo TxGNN predice que podría ser efectivo para **uretritis por Ureaplasma**, pero **no hay ensayos clínicos** y las **4 publicaciones** recuperadas tratan la uretritis en general, sin respaldar esta indicación concreta. Entre las predicciones evaluadas, la **uretritis gonocócica** es la más sólida (9 publicaciones, varios estudios clínicos de los años 80), aunque corresponde a un uso antibacteriano ya conocido y no a un reposicionamiento genuino.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Amoxicilina y inhibidor de betalactamasa |
| Nueva Indicación Predicha | Uretritis por Ureaplasma |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, el ácido clavulánico es un inhibidor de betalactamasas que se combina con amoxicilina; su utilidad en infecciones bacterianas está establecida, y protege a la amoxicilina de la degradación por enzimas bacterianas.

Para **Ureaplasma**, la predicción **no es mecanísticamente plausible**. Ureaplasma carece de pared celular, por lo que las combinaciones de betalactámico con inhibidor no se esperan efectivas. El puntaje alto probablemente refleja asociaciones generales entre uretritis e infecciones bacterianas genitourinarias, y no actividad específica contra este organismo. La literatura recuperada trata la uretritis en general y no respalda eficacia frente a Ureaplasma.

Otras predicciones del modelo con mejor fundamento mecanístico:
- **Uretritis gonocócica** (puntaje 99.93%, nivel L3): el clavulanato inhibe la penicilinasa de *Neisseria gonorrhoeae* resistente y restaura la actividad de la amoxicilina. Varios estudios de los años 80 reportan eficacia en hombres. Sin embargo, la evidencia es histórica, de estudios pequeños, y anterior a la resistencia actual; las guías vigentes prefieren esquemas basados en ceftriaxona.
- **Enfermedad inflamatoria uterina** (L4): plausible en infecciones polimicrobianas, pero la mayoría de la literatura es veterinaria o de modelos animales.
- **Tuberculosis urogenital** (L5): *M. tuberculosis* produce una betalactamasa (BlaC) inhibida por clavulanato, pero no hay evidencia clínica.
- Las demás predicciones (síndrome de compresión del tronco celíaco, embarazo ectópico abdominal, linfangioma quístico abdominal, miofibroblastoma en empalizada de ganglio linfático) carecen de base mecanística y probablemente reflejan artefactos de la red.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la indicación principal (uretritis por Ureaplasma):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Revisión | Rev Esp Quimioter | Mejor tratamiento empírico de la uretritis en el centro de Madrid; no específico de Ureaplasma |
| [19544099](https://pubmed.ncbi.nlm.nih.gov/19544099/) | 2009 | Revisión | Rev Esp Quimioter | Prevalencia y tendencia de los microorganismos causantes de uretritis en hombres |
| [9669200](https://pubmed.ncbi.nlm.nih.gov/9669200/) | 1998 | Revisión | Int J Androl | Posible papel de bacterias anaerobias en la prostatitis crónica |
| [34366085](https://pubmed.ncbi.nlm.nih.gov/34366085/) | 2021 | Reporte de caso | Infect Dis Now | Primera asociación de *Pasteurella bettyae* con uretritis y balanitis |

Ninguna de estas publicaciones evalúa el ácido clavulánico frente a Ureaplasma.

Para la uretritis gonocócica (predicción alternativa con mayor respaldo):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3533755](https://pubmed.ncbi.nlm.nih.gov/3533755/) | 1986 | Ensayo clínico comparativo aleatorizado | Genitourin Med | Cefuroxima axetilo vs. amoxicilina + ácido clavulánico en 500 pacientes con gonorrea urogenital y rectal no complicada |
| [6365235](https://pubmed.ncbi.nlm.nih.gov/6365235/) | 1984 | Ensayo clínico comparativo | Br J Vener Dis | Amoxicilina 3 g + clavulanato 250 mg vs. penicilina procaína IM en 121 hombres: persistencia de cultivo positivo 9.4% vs. 26.3% |
| [6428699](https://pubmed.ncbi.nlm.nih.gov/6428699/) | 1984 | Estudio clínico | Br J Vener Dis | Augmentin en dos dosis vs. kanamicina en 192 hombres: curación 95.9% vs. 87.4% |
| [4007860](https://pubmed.ncbi.nlm.nih.gov/4007860/) | 1985 | Estudio clínico | Genitourin Med | Amoxicilina 3 g + clavulanato 125 mg curó 97 de 100 pacientes evaluables con gonorrea anogenital no complicada |
| [3004176](https://pubmed.ncbi.nlm.nih.gov/3004176/) | 1985 | Estudio clínico | Afr J Med Med Sci | Augmentin en dosis única en Ibadán, donde ~80% de las cepas producen penicilinasa |
| [6757686](https://pubmed.ncbi.nlm.nih.gov/6757686/) | 1982 | Estudio clínico | Med J Malaysia | Amoxicilina y ácido clavulánico en dosis única oral en hombres con uretritis gonocócica |
| [3147528](https://pubmed.ncbi.nlm.nih.gov/3147528/) | 1988 | Estudio clínico | Sex Transm Dis | Opciones terapéuticas para gonorrea por cepas resistentes, incluida amoxicilina con clavulanato |
| [3132029](https://pubmed.ncbi.nlm.nih.gov/3132029/) | 1988 | Estudio microbiológico | Hinyokika Kiyo | Detección de *N. gonorrhoeae* productora de penicilinasa y sensibilidad a amoxicilina/clavulanato |
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Revisión | Rev Esp Quimioter | Tratamiento empírico de la uretritis |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20189193 (cancelado) | AMOXIDAL PLUS 600 POLVO PARA RECONSTITUIR A SUSPENSION ORAL | Polvo para reconstituir a suspensión oral | Amoxicilina y inhibidor de betalactamasa |

Fabricante: Megalabs Colombia S.A.S. No hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según el grafo de conocimiento TxGNN, no según prospecto):** enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, colitis por *Clostridium difficile*, enterocolitis necrotizante perinatal, colestasis (incluidas la colestasis intrahepática recurrente benigna y la familiar), mononucleosis infecciosa y síndrome de infección crónica por virus de Epstein-Barr.
- **Interacciones farmacológicas:** se identificaron 16 interacciones. Las de nivel **mayor** son con **leflunomida** y **teriflunomida**. Las de nivel moderado incluyen metotrexato, naltrexona, balsalazida, asparaginasa, pegaspargasa, brentuximab vedotina, clofarabina, epirrubicina, idelalisib, interferón beta-1a, interferón beta-1b, peginterferón beta-1a, tioguanina y trabectedina.

No se dispone de advertencias ni contraindicaciones del prospecto; se debe consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (uretritis por Ureaplasma) no tiene respaldo mecanístico, pues Ureaplasma carece de pared celular, ni evidencia clínica (nivel L5). La única alternativa con evidencia (uretritis gonocócica, L3) corresponde a un uso antibacteriano histórico, superado por las guías actuales basadas en ceftriaxona, y el producto colombiano tiene su registro cancelado.

**Para avanzar se necesita:**
- Revisar el prospecto oficial de INVIMA (advertencias y contraindicaciones).
- Obtener datos del mecanismo de acción desde DrugBank.
- Evaluar si la uretritis gonocócica merece seguimiento como pregunta de investigación, considerando la resistencia actual y las guías vigentes.
- Descartar la indicación por Ureaplasma salvo que aparezca evidencia microbiológica o clínica específica.
- Confirmar si existen otros registros sanitarios vigentes de amoxicilina/ácido clavulánico en Colombia, ya que el único registro identificado está cancelado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

