---
layout: default
title: Rifabutin
parent: Evidencia Alta (L1-L2)
nav_order: 557
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Rifabutin: nueva indicación predicha, Infección por VIH (en la práctica… (nivel de evidencia L1). Indicación original: RIFABUTIN"
monitor_inn: "rifabutin"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "sclerosing cholangitis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "conjunctivitis", "leprosy", "endocarditis", "pneumocystosis", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
---

# Rifabutin
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Rifabutina: De Rifabutina (indicación registrada) a Infección por VIH (enfermedades micobacterianas asociadas al VIH)
{: .text-alpha }

## Resumen en Una Frase

Rifabutina es un antibiótico antimicobacteriano del grupo de las rifamicinas, registrado en Colombia bajo el texto de indicación "RIFABUTIN".
El modelo TxGNN predice que podría ser efectivo para **infección por VIH**, aunque la evidencia real apunta a infecciones micobacterianas asociadas al VIH (complejo *Mycobacterium avium* y tuberculosis con VIH), no al virus en sí.
Actualmente hay **34 ensayos clínicos** y **20 publicaciones** compilados que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | RIFABUTIN (el registro sanitario no detalla una indicación específica) |
| Nueva Indicación Predicha | Infección por VIH (en la práctica, enfermedad micobacteriana asociada al VIH) |
| Puntaje de Predicción TxGNN | 0.9988 |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, rifabutina es una rifamicina que inhibe la ARN polimerasa dependiente de ADN bacteriana. Su eficacia contra micobacterias está comprobada.

Rifabutina **no es un antiviral**. Su relevancia en el VIH es indirecta: se usa en infecciones oportunistas como la profilaxis y el tratamiento del complejo *Mycobacterium avium* (MAC) y en la coinfección tuberculosis/VIH. Frente a rifampicina, induce menos la enzima CYP3A y es más compatible con los inhibidores de proteasa, por lo que suele ser la rifamicina preferida en pacientes con estos antirretrovirales.

Por tanto, la predicción del modelo es razonable si se interpreta como "enfermedad micobacteriana asociada al VIH". Requiere ajuste de dosis con inhibidores de proteasa (p. ej., lopinavir/ritonavir, indinavir) y precaución con los regímenes de acción prolongada de cabotegravir/rilpivirina.

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes de los 34 compilados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Fase 3 | Completado | 450 | Claritromicina/etambutol con rifabutina (dos dosis) o placebo en bacteriemia por MAC en SIDA |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Fase 3 | Completado | 400 | Cuatro regímenes (claritromicina con etambutol y rifabutina o clofazimina) en MAC diseminado con SIDA |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Fase 3 | Completado | 1100 | Claritromicina vs. rifabutina vs. combinación para prevenir MAC en VIH con CD4 ≤100 |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Fase 3 | Completado | 720 | Azitromicina y rifabutina, solas o combinadas, para prevenir MAC diseminado en VIH |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | N/A | Completado | 200 | Ensayo doble ciego de un régimen con rifabutina en bacteriemia por MAC en SIDA |
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | N/A | Completado | 750 | Rifabutina vs. placebo para prevenir bacteriemia por MAC con CD4 ≤200 |
| [NCT00001058](https://clinicaltrials.gov/study/NCT00001058) | Fase 2 | Completado | 246 | Tres regímenes con claritromicina (con rifabutina, etambutol o ambos) en MAC diseminado |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Fase 2 | Completado | 47 | Farmacocinética de rifabutina con antirretrovirales en tuberculosis/VIH (Vietnam) |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Fase 2 | Completado | 48 | Farmacocinética de rifabutina con antirretrovirales en tuberculosis/VIH (Sudáfrica) |
| [NCT00000877](https://clinicaltrials.gov/study/NCT00000877) | Fase 1 | Completado | 31 | Interacción farmacocinética en estado estable entre indinavir y rifabutina |

## Evidencia de Literatura

Se muestran las publicaciones más relevantes de las 20 compiladas.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33740465](https://pubmed.ncbi.nlm.nih.gov/33740465/) | 2021 | ECA (Fase 2) | Lancet Respir Med | Terapias adyuvantes dirigidas al huésped en tuberculosis pulmonar; seguridad y eficacia preliminar |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohorte | J Antimicrob Chemother | Farmacocinética y seguridad de rifabutina en niños con TB/VIH que reciben lopinavir/ritonavir |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohorte | J Antimicrob Chemother | Seguridad y eficacia de rifabutina en niños con TB/VIH; se reportó neutropenia que limitó el tratamiento |
| [23828580](https://pubmed.ncbi.nlm.nih.gov/23828580/) | 2013 | Revisión sistemática | Cochrane Database Syst Rev | Rifamicinas vs. isoniazida para prevenir tuberculosis en personas VIH negativas |
| [21819645](https://pubmed.ncbi.nlm.nih.gov/21819645/) | 2012 | Revisión | Int J Tuberc Lung Dis | Uso de rifabutina como alternativa a rifampicina con antirretrovirales con inhibidores de proteasa |
| [17181373](https://pubmed.ncbi.nlm.nih.gov/17181373/) | 2006 | Revisión | Drugs | Enfoque terapéutico práctico de la coinfección TB/VIH |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Revisión | Microbiol Spectr | Tuberculosis asociada a la infección por VIH |
| [36377436](https://pubmed.ncbi.nlm.nih.gov/36377436/) | 2023 | Estudio de modelado | Clin Infect Dis | Manejo de interacciones de cabotegravir/rilpivirina de acción prolongada con inductores como rifabutina |
| [9093233](https://pubmed.ncbi.nlm.nih.gov/9093233/) | 1997 | Revisión | Med Clin North Am | Infecciones por micobacterias no tuberculosas, con MAC como infección sistémica más común en SIDA |
| [11996607](https://pubmed.ncbi.nlm.nih.gov/11996607/) | 2002 | Revisión | Arch Intern Med | Actualización de interacciones farmacológicas de rifampicina y rifabutina |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20155669 (cancelado) | RIFBUTIN® 150 MG CAPSULAS | Cápsula dura | RIFABUTIN |

## Citotoxicidad

Rifabutina es un antibiótico antimicobacteriano y no un fármaco antineoplásico; por ello no se aplica una clasificación de citotoxicidad.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: trombocitopenia, neutropenia, agranulocitosis, colitis por *Clostridium difficile* y enterocolitis necrosante perinatal. La literatura compilada también describe neutropenia que limitó el tratamiento en niños con TB/VIH.
- **Interacciones farmacológicas**: se identificaron 163 interacciones. Entre las listadas, la única de gravedad **mayor** es **eliglustat**. Las de gravedad **moderada** incluyen doxiciclina, claritromicina, metronidazol, corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona), morfina, aprepitant, pioglitazona y otros antidiabéticos (clorpropamida, acetohexamida, saxagliptina, linagliptina), además de vitamina D y derivados (colecalciferol, calcifediol, calcitriol) y ácido picosulfúrico. La de dolasetrón es **menor**.
- Además, rifabutina es inductora de CYP3A y requiere ajuste de dosis con inhibidores de proteasa y precaución con antirretrovirales de acción prolongada.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de Fase 3 completados con rifabutina en MAC asociado al VIH, por lo que el nivel de evidencia es L1. Sin embargo, la evidencia respalda el uso en infecciones micobacterianas asociadas al VIH y no un efecto antiviral, y el único registro sanitario local está cancelado.

**Para avanzar se necesita:**
- Redefinir la indicación como "infecciones micobacterianas asociadas al VIH" (MAC y tuberculosis/VIH), no como VIH en sí.
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones) y los datos de mecanismo de acción en DrugBank.
- Verificar la situación regulatoria en Colombia, ya que no hay registro vigente.
- Definir un plan de manejo de interacciones (inhibidores de proteasa, cabotegravir/rilpivirina) y monitoreo hematológico por riesgo de neutropenia, especialmente en población pediátrica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

