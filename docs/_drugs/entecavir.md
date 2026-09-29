---
layout: default
title: Entecavir
parent: Solo Predicción del Modelo (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: De Hepatitis B Crónica a Infección Crónica por Virus de la Hepatitis C

## Resumen en Una Frase

Entecavir es un análogo nucleósido de guanosina que se usa para tratar la hepatitis B crónica. El registro INVIMA solo consigna el nombre «ENTECAVIR», sin texto de indicación.
El modelo TxGNN predice que podría ser efectivo para **infección crónica por el virus de la hepatitis C**, pero esa predicción no tiene respaldo directo.
Se recuperaron **40 ensayos clínicos** y **20 publicaciones** asociados a la predicción. Ninguno evalúa entecavir como tratamiento del VHC: todos tratan hepatitis B o coinfección VHB/VHC, donde entecavir actúa solo sobre el VHB.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hepatitis B crónica (según la evidencia recuperada; el registro INVIMA solo indica «ENTECAVIR») |
| Nueva Indicación Predicha | Infección crónica por el virus de la hepatitis C |
| Puntaje de Predicción TxGNN | 99.98% (posición 350) |
| Nivel de Evidencia | L4 (según el paquete de evidencia; sin evidencia directa de eficacia contra VHC) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es razonable esta predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente de DrugBank de este paquete. Por conocimiento general, entecavir es un análogo de guanosina. Su forma trifosfato compite con la dGTP e inhibe la polimerasa del VHB (cebado, transcripción inversa y síntesis de ADN). Ese mecanismo es directo y está bien establecido, pero es específico del virus de la hepatitis B.

El VHC es un virus de ARN que se replica mediante la polimerasa NS5B, y no se conoce que entecavir la inhiba. El puntaje alto de TxGNN probablemente refleja que el modelo agrupa las hepatitis virales en la red de conocimiento (fármacos, genes y enfermedades vecinos). No refleja un efecto antiviral directo contra el VHC.

La relación entre ambas indicaciones es clínica, no mecanística. El VHB y el VHC comparten vías de transmisión y muchos pacientes tienen coinfección. Entecavir se usa en esos pacientes para controlar el VHB, por ejemplo para prevenir su reactivación durante el tratamiento del VHC con antivirales de acción directa. Por eso la predicción parece un artefacto del grafo y no una oportunidad real de reposicionamiento.

## Evidencia de Ensayos Clínicos

Se listan 10 de los 40 ensayos recuperados, los más cercanos al contexto VHC/VHB. Ninguno prueba entecavir contra el VHC.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Antivirales de acción directa en coinfección VHC/VHB. Estudia la reactivación del VHB durante el tratamiento anti-VHC. Entecavir no es el agente evaluado (contexto indirecto). |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Desconocido | 60 | Análogos nucleós(t)idos como profilaxis de la reactivación del VHB en coinfectados VHC/VHB que reciben antivirales para VHC. Compara 12 frente a 24 semanas. El registro no especifica que el análogo sea entecavir. |
| [NCT03662568](https://clinicaltrials.gov/study/NCT03662568) | Fase 1 | Completado | 56 | Interacción farmacológica y farmacocinética de morfotiadina/ritonavir con entecavir o tenofovir en voluntarios sanos. Sin datos de eficacia contra VHC. |
| [NCT00065507](https://clinicaltrials.gov/study/NCT00065507) | Fase 3 | Completado | 195 | Entecavir frente a adefovir en infección crónica por VHB con descompensación hepática. Es evidencia de VHB, no de VHC. |
| [NCT01354652](https://clinicaltrials.gov/study/NCT01354652) | Fase 4 | Terminado | 5 | Incidencia de acidosis láctica con entecavir en hepatitis B con cirrosis grave o insuficiencia hepática. Estudio de seguridad terminado con muy pocos participantes. |
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | N/A | Desconocido | 420 | Entecavir en hepatitis B de pacientes con carcinoma hepatocelular tratados con ablación por radiofrecuencia. Es un estudio de VHB. |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | Completado | 130 | Arabinoxilano de salvado de arroz en carcinoma hepatocelular y hepatitis B y C. No evalúa entecavir. |
| [NCT00371150](https://clinicaltrials.gov/study/NCT00371150) | Fase 4 | Completado | 131 | Efecto antiviral de entecavir en pacientes afroamericanos e hispanos con hepatitis B crónica sin tratamiento previo. |
| [NCT01848743](https://clinicaltrials.gov/study/NCT01848743) | Fase 3 | Desconocido | 120 | Tenofovir frente a lamivudina en exacerbación aguda grave de hepatitis B crónica. Entecavir no es el fármaco evaluado. |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Fase 2/3 | Completado | 120 | Estudio piloto de interferón alfa-2b con ribavirina en hepatitis B crónica. No evalúa entecavir. |

## Evidencia de Literatura

Se listan 10 de las 20 publicaciones recuperadas. No hay ECA, y ninguna muestra que entecavir sea eficaz contra el VHC.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohorte | Viruses | 66 pacientes con hepatitis B crónica y anti-VHC positivos, tratados con análogos nucleós(t)idos. Evalúa si el VHC se reactiva tras el tratamiento anti-VHB. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Revisión | Expert Opin Pharmacother | Avances en el tratamiento de la coinfección VHB/VHC, que conlleva alto riesgo de cirrosis y carcinoma hepatocelular. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Revisión | Wien Med Wochenschr | Tratamiento actual y perspectivas en hepatitis B y C crónicas, con foco en interferón pegilado y lamivudina. |
| [32527114](https://pubmed.ncbi.nlm.nih.gov/32527114/) | 2021 | Revisión | Chin Clin Oncol | Momento y manejo de la hepatitis B y C en pacientes con carcinoma hepatocelular. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | No clasificado | Minerva Gastroenterol Dietol | Antivirales para hepatitis B y C y sus efectos sobre la función renal. |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | No clasificado | J Gastroenterol Hepatol | Riesgo de reactivación del VHB durante el tratamiento del VHC con antivirales de acción directa. |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | No clasificado | World J Hepatol | Manejo de hepatitis B y C antes y después del trasplante de hígado y riñón. Los análogos de alta barrera genética, como entecavir y tenofovir, mejoran el pronóstico en VHB. |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Reporte de caso | Clin Res Hepatol Gastroenterol | Paciente coinfectado con VHB y VHC. Describe el tratamiento de la coinfección como un desafío terapéutico. |
| [36873880](https://pubmed.ncbi.nlm.nih.gov/36873880/) | 2023 | Reporte de caso | Front Med | Evolución viral inusual tras antivirales en un paciente con VHB y VHC simultáneos. |
| [39036171](https://pubmed.ncbi.nlm.nih.gov/39036171/) | 2024 | Reporte de caso | Cureus | Colapso dinámico excesivo de la vía aérea tras entecavir en un paciente con enfermedad del tejido conectivo inducida por interferón pegilado. Es un reporte de seguridad. |

## Información de Mercado en Colombia

El registro contiene 5 entradas, pero solo 2 números de registro distintos (las demás repiten los mismos registros). El paquete indica 10 registros sanitarios en total. Ambos productos son del fabricante Bristol Myers Squibb de Colombia S.A.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19964164 | BARACLUDE TABLETA RECUBIERTA 1MG | Tableta recubierta | Solo consigna «ENTECAVIR» (sin texto de indicación) |
| 19964241 | BARACLUDE TABLETA RECUBIERTA 0.5 MG | Tableta recubierta | Solo consigna «ENTECAVIR» (sin texto de indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- No hay evidencia directa de que entecavir actúe contra el VHC, y no se conoce que inhiba la polimerasa NS5B. Los 40 ensayos y 20 publicaciones recuperados tratan hepatitis B o coinfección, donde entecavir solo trata el componente VHB.
- El puntaje TxGNN de 99.98% probablemente refleja la cercanía entre hepatitis virales en el grafo de conocimiento y no un efecto antiviral real. El VHC además ya tiene antivirales de acción directa curativos.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones, que hoy bloquean el tamizaje de seguridad.
- Obtener el mecanismo de acción detallado desde DrugBank.
- Comprobar, con ensayos in vitro (replicón de VHC), si entecavir tiene algún efecto sobre el VHC. Sin ese dato no hay base para reposicionarlo.
- Si el interés real es la coinfección VHB/VHC, replantear el caso como profilaxis de la reactivación del VHB durante el tratamiento anti-VHC. Es un uso del VHB, no un reposicionamiento hacia VHC.
- Vigilar, en cualquier escenario, la función renal, la acidosis láctica, la trombocitopenia (PMID 34823407), la resistencia y las exacerbaciones de hepatitis B tras suspender el tratamiento.

**Nota:** la segunda predicción del modelo, infección por el virus de la hepatitis B (L1, Proceed with Guardrails), corresponde a la indicación ya establecida de entecavir. Es una indicación recuperada, no un reposicionamiento nuevo.

*Los resultados son solo para referencia de investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

