---
layout: default
title: Abacavir
parent: Evidencia Moderada (L3-L4)
nav_order: 11
evidence_level: L4
indication_count: 3
---

# Abacavir
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Abacavir: De Infección por VIH a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Abacavir es un inhibidor nucleósido de la transcriptasa inversa (NRTI). En Colombia se comercializa en combinaciones antirretrovirales de dosis fija con lamivudina y con zidovudina más lamivudina.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina (FIV)**.
Hay **4 ensayos clínicos** y **1 publicación**, pero todos los ensayos son en VIH-1 humano y la única publicación es un estudio *in vitro*. La evidencia directa es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro INVIMA solo lista la composición de la combinación ("ABACAVIR/ZIDOVUDINA/LAMIVUDINA"), no un texto de indicación. El uso conocido de estas combinaciones es la infección por VIH. |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome) |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción curados en la base de datos. Según la farmacología general, abacavir es un análogo nucleósido carbocíclico de guanosina. Dentro de la célula se fosforila a carbovir trifosfato, que detiene la elongación del ADN viral.

El FIV es un lentivirus con transcriptasa inversa, muy similar al VIH a nivel molecular y clínico. Por eso el gato doméstico se usa como modelo animal del VIH, y varios inhibidores de la transcriptasa inversa activos contra el VIH también lo son contra el FIV. La actividad de abacavir contra el FIV es, por tanto, mecanísticamente plausible.

El puntaje alto de TxGNN probablemente refleja el papel conocido de abacavir contra el VIH-1 y la cercanía entre los nodos de VIH y FIV en el grafo de conocimiento. Este vínculo se apoya en farmacología general y no en un registro curado. Además, el FIV es una enfermedad veterinaria y no una indicación humana, lo que limita su relevancia para el mercado colombiano de medicamentos de uso humano.

---

## Evidencia de Ensayos Clínicos

Los cuatro ensayos son en VIH-1 humano. Ninguno evalúa el FIV, y abacavir es parte del esquema de fondo, no el objeto de estudio.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Fase 3 | Completado | 844 | Dolutegravir + abacavir/lamivudina vs Atripla durante 96 semanas en adultos con VIH-1 sin tratamiento previo. Apoya la eficacia y seguridad antirretroviral en humanos (relevancia: B). |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Fase 2 | Completado | 208 | Estudio de selección de dosis de dolutegravir con abacavir/lamivudina o tenofovir/emtricitabina. Abacavir es parte del esquema, pero no el objeto de evaluación (relevancia: B). |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Fase 3 | Completado | 828 | Dolutegravir vs raltegravir con abacavir/lamivudina o tenofovir/emtricitabina como base. Abacavir es solo una de las opciones de base (relevancia: C). |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Fase 3 | Completado | 13 | Estudio de un solo brazo de dolutegravir + abacavir/lamivudina, con farmacocinética en plasma y líquido cefalorraquídeo. Evidencia indirecta (relevancia: C). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Estudio *in vitro* (tipo no verificado) | Antiviral Research | Efecto combinado de zidovudina, lamivudina y abacavir para suprimir la replicación del FIV *in vitro*. El FIV se usa como modelo animal del VIH y varios inhibidores de la transcriptasa inversa activos contra el VIH también lo son contra el FIV. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20203375 | SELMIVIR® | Tableta recubierta | Abacavir/zidovudina/lamivudina (solo composición) |
| 20140104 | KAVIDUVIR® tableta recubierta | Tableta recubierta | Lamivudina y abacavir (solo composición) |

Los datos traen 5 filas, pero 4 corresponden al mismo registro 20203375, por lo que se muestran solo los 2 registros únicos. El total informado es de 8 registros sanitarios.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción del FIV es mecanísticamente plausible, pero solo tiene un estudio *in vitro* de 2002 como respaldo directo. Los ensayos de Fase 2/3 son en VIH-1 humano y no sirven como evidencia de eficacia en FIV. Además, no hay datos de seguridad del prospecto INVIMA.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones).
- Obtener el mecanismo de acción curado desde DrugBank.
- Verificar el tipo de estudio y el modelo del PMID 11684314 (hoy sin confirmar).
- Buscar estudios veterinarios o en modelo felino específicos de abacavir.
- Definir si una indicación veterinaria es relevante para el alcance del proyecto en Colombia.

**Otras predicciones:** el modelo también sugiere infección por virus de inmunodeficiencia de simios (SIV, L4, solo un estudio *in vitro* indirecto, Hold) y un trastorno del neurodesarrollo raro (L5, sin evidencia ni vínculo mecanístico, Hold). Ninguna de las dos debe orientar decisiones por ahora.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

