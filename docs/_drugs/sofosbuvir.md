---
layout: default
title: Sofosbuvir
parent: Evidencia Moderada (L3-L4)
nav_order: 589
evidence_level: L3
indication_count: 8
last_modified_at: 2026-11-25
description: "Sofosbuvir: nueva indicación predicha, Infección por virus de la hepatitis B (nivel de evidencia L3). Indicación original: Sofosbuvir + Velpatasvir (hepatitis C crónica)"
monitor_inn: "SOFOSBUVIR"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever", "chronic hepatitis B virus infection", "Kyasanur forest disease", "HIV infectious disease"]
---

# Sofosbuvir
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **8** 
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

## Sofosbuvir: De Hepatitis C (Sofosbuvir + Velpatasvir) a Infección por Virus de la Hepatitis B
{: .text-alpha }

## Resumen en Una Frase

Sofosbuvir es un análogo de nucleótido inhibidor de la polimerasa NS5B del VHC, registrado en Colombia como parte de la combinación sofosbuvir + velpatasvir (Epclusa®).
El modelo TxGNN predice que podría ser efectivo para **infección por virus de la hepatitis B**, con **10 ensayos clínicos** y **20 publicaciones** asociados a esta predicción. Sin embargo, casi toda esta evidencia proviene de pacientes con coinfección VHC/VHB, donde el beneficio es indirecto y existe un riesgo de reactivación del VHB.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sofosbuvir + Velpatasvir (hepatitis C crónica) |
| Nueva Indicación Predicha | Infección por virus de la hepatitis B |
| Puntaje de Predicción TxGNN | 0.9977 |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Sofosbuvir (traducción no oficial): «El sofosbuvir es un antiviral de acción directa contra el virus de la hepatitis C. […] El sofosbuvir es un inhibidor de la ARN polimerasa dependiente de ARN NS5B del VHC, que es esencial para la replicación viral. El sofosbuvir es un profármaco nucleotídico que se metaboliza a nivel intracelular para formar el trifosfato análogo de uridina farmacológicamente activo (GS-461203), que puede ser incorporado al ARN del VHC por la polimerasa NS5B y actúa como terminador de cadena.» Texto original en inglés: "Sofosbuvir is a direct-acting antiviral agent against the hepatitis C virus. […] Sofosbuvir is an inhibitor of the HCV NS5B RNA-dependent RNA polymerase, which is essential for viral replication. Sofosbuvir is a nucleotide prodrug that undergoes intracellular metabolism to form the pharmacologically active uridine analog triphosphate (GS-461203), which can be incorporated into HCV RNA by the NS5B polymerase and acts as a chain terminator." ([DailyMed: Sovaldi (sofosbuvir) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=80beab2c-396e-4a37-a4dc-40fdb62859cf), versión del 2024-12-26; consultado el 2026-11-19). Según la información conocida, sofosbuvir es un análogo de nucleótido que inhibe la ARN polimerasa dependiente de ARN (NS5B) del virus de la hepatitis C, y su eficacia en hepatitis C está bien establecida.

La relación con la hepatitis B es débil desde el punto de vista mecanístico. El VHB se replica mediante una ADN polimerasa/transcriptasa inversa, por lo que no hay una coincidencia directa con el blanco de sofosbuvir. Los datos clínicos en VHB provienen sobre todo de pacientes coinfectados VHC/VHB, en los que el tratamiento con antivirales de acción directa no suprime el VHB y puede desencadenar su reactivación. Por ello, no se espera que sofosbuvir tenga actividad anti-VHB intrínseca, y el puntaje tan alto del modelo (0.9977) no está respaldado por este razonamiento.

Existe un estudio de Fase 2 de ledipasvir/sofosbuvir en monoinfección por VHB que reporta una reducción modesta del HBsAg, lo que puede considerarse una señal exploratoria que requiere confirmación.

Entre las demás predicciones de la lista, la **hepatitis E** (rango 2) tiene un fundamento mecanístico más plausible, ya que el VHE posee una ARN polimerasa dependiente de ARN. Los datos in vitro muestran inhibición de la replicación viral, pero los resultados clínicos son modestos y sin depuración viral sostenida. La **hepatitis B crónica** (rango 6) comparte las mismas limitaciones que la hepatitis B general. Las predicciones de hepatitis viral animal, hepatitis A, fiebre hemorrágica de Omsk, enfermedad del bosque de Kyasanur y VIH están respaldadas solo por evidencia preclínica o indirecta, o por ninguna.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Fase 2 | Completado | 21 | Ledipasvir/sofosbuvir por 12 semanas en infección por VHB; estudio abierto de un solo brazo, informa sobre seguridad y comportamiento del VHB, no eficacia |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Antivirales de acción directa en coinfección VHC/VHB; evalúa la reactivación del VHB durante el tratamiento anti-VHC |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Fase 4 | Desconocido | 120 | SOF/VEL con TAF profiláctico en coinfección VHC/VHB; la actividad anti-VHB proviene del TAF |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Fase 2 | Desconocido | 21 | Ledipasvir/sofosbuvir en linfoma de células B asociado a VHC; evidencia indirecta para VHB |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Fase 4 | Desconocido | 25 | Cambio a E/C/F/TAF seguido de SOF/VEL en coinfección VIH-VHC; el efecto anti-VHB lo aporta el tenofovir alafenamida |
| [NCT03186313](https://clinicaltrials.gov/study/NCT03186313) | Fase 3 | Completado | 72 | Combinación de dosis única con sofosbuvir y daclatasvir en VHC genotipo 4; relevancia limitada para VHB |
| [NCT02363517](https://clinicaltrials.gov/study/NCT02363517) | Fase 3 | Desconocido | 420 | Tratamiento del VHC con sofosbuvir + ledipasvir en personas que se inyectan drogas; sin datos de eficacia en VHB |
| [NCT02483156](https://clinicaltrials.gov/study/NCT02483156) | Fase 2/3 | Completado | 80 | Sofosbuvir + ribavirina en VHC genotipo 4; relevancia indirecta |
| [NCT02768961](https://clinicaltrials.gov/study/NCT02768961) | Fase 4 | Completado | 64 | Programa de cribado y eliminación del VHC en prisiones; no relevante para eficacia en VHB |
| [NCT03579576](https://clinicaltrials.gov/study/NCT03579576) | N/A | Completado | 803 | Estrategia simplificada de tratamiento del VHC en Myanmar; no evalúa VHB |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Ensayo Fase 2 abierto | J Med Virol | Ledipasvir/sofosbuvir por 12 semanas en monoinfección por VHB; se evaluó el descenso de HBsAg y ADN del VHB |
| [42558970](https://pubmed.ncbi.nlm.nih.gov/42558970/) | 2026 | Estudio clínico | J Clin Transl Hepatol | Seguridad y eficacia de SOF/VEL con pretratamiento con TAF en coinfección VHB/VHC, para prevenir la reactivación del VHB |
| [35268497](https://pubmed.ncbi.nlm.nih.gov/35268497/) | 2022 | Cohorte | J Clin Med | Cinética de ADN del VHB y HBsAg en pacientes coinfectados durante el tratamiento con antivirales de acción directa |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohorte/Observacional | J Clin Gastroenterol | Riesgo de reactivación del VHB durante el tratamiento con ledipasvir-sofosbuvir |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Estudio observacional prospectivo | J Viral Hepat | Reactivación del VHB en pacientes con cáncer que reciben antivirales de acción directa para VHC |
| [26967675](https://pubmed.ncbi.nlm.nih.gov/26967675/) | 2016 | Revisión | J Clin Virol | La reactivación del VHB en la coinfección es un desafío del tratamiento con antivirales de acción directa |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Revisión | Minerva Gastroenterol Dietol | Antivirales para hepatitis B y C y sus efectos sobre la función renal |
| [39914746](https://pubmed.ncbi.nlm.nih.gov/39914746/) | 2025 | Revisión | J Hepatol | Lecciones del tratamiento del VHC aplicables a nuevas terapias para VHB y VHD |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | Reporte de reacciones adversas | Hosp Pharm | Reactivación de hepatitis B con simeprevir y sofosbuvir |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Revisión | Acta Pharm Sin B | Panorama de los antivirales de acción directa contra el VHC |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20126648 | EPCLUSA® | TABLETA RECUBIERTA | SOFOSBUVIR + VELPATASVIR | Vigente |
| 20092040 | SOVALDI® | TABLETA RECUBIERTA | SOFOSBUVIR | Temp. no comerc - Vigente |
| 20106277 | HARVONI® | TABLETA RECUBIERTA | SOFOSBUVIR Y LEDIPASVIR | Temp. no comercializado - En Trámite Renov |

Se muestran los 3 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (8 interacciones identificadas):
  - **Mayor**: apalutamida, enzalutamida, lorlatinib
  - **Moderada**: fostamatinib, warfarina, dicumarol, encorafenib
  - **Menor**: ciclosporina
- **Reactivación del VHB**: la literatura revisada documenta reactivación del virus de la hepatitis B en pacientes coinfectados que reciben antivirales de acción directa contra el VHC, incluido sofosbuvir. Esto es especialmente relevante para esta nueva indicación.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje de TxGNN es muy alto, la evidencia disponible es indirecta (coinfección VHC/VHB) y no respalda un efecto anti-VHB de sofosbuvir. No hay coincidencia mecanística directa con la polimerasa del VHB y existe riesgo documentado de reactivación. Además, no se dispone de datos de advertencias ni contraindicaciones del prospecto.

<!-- review:begin co-lic-20261105-sofosbuvir-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado, y no se dispone de datos de advertencias ni contraindicaciones del prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-sofosbuvir-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío de información que bloquea el cribado de seguridad
- Resultados completos y confirmatorios en monoinfección por VHB (el estudio de Fase 2 de ledipasvir/sofosbuvir es de un solo brazo y pequeño)
- Considerar, como líneas de investigación con más respaldo mecanístico, la hepatitis E (el ensayo de Fase 2 SofE mostró reducción inicial de la carga viral pero sin respuesta virológica sostenida y con variantes asociadas a resistencia)
- Aclarar la situación regulatoria en Colombia

<!-- review:begin co-lic-20261105-sofosbuvir-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria en Colombia, dado que el registro de Epclusa® figura como cancelado" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-sofosbuvir-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado, y" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que el registro de Epclusa® figura como cancelado" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Sovaldi (sofosbuvir) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=80beab2c-396e-4a37-a4dc-40fdb62859cf) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

