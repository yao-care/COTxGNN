---
layout: default
title: Polidocanol
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# Polidocanol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Polidocanol: De Várices Varicosas a Várices Esofágicas con Hemorragia

## Resumen en Una Frase

Polidocanol es un agente esclerosante aprobado globalmente para el tratamiento de várices superficiales (varices varicosas) y telangiectasias (arañas vasculares). El modelo TxGNN predice que podría ser efectivo para **Várices Esofágicas con Hemorragia**, con **7 ensayos clínicos** y **20 publicaciones** que respaldan actualmente esta dirección. Esta predicción representa una extensión mecanísticamente coherente de su indicación original hacia la vía endoscópica intraluminal, respaldada por evidencia clínica histórica desde los años 1980.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Várices varicosas y telangiectasias (arañas vasculares) |
| Nueva Indicación Predicha | Várices esofágicas con hemorragia |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Polidocanol (también conocido como Aethoxysklerol, Lauromacrogol o etoxisclerol) es un agente esclerosante de la clase de los polietilenglicol-éteres, que actúa como surfactante anfifílico. Cuando se inyecta directamente en la pared de una vena varicosa, destruye la bicapa lipídica de la membrana endotelial, induciendo daño endotelial agudo y trombosis local, lo que conduce a la obliteración y esclerosis progresiva de la vena. Este mecanismo es idéntico al de su indicación aprobada para várices superficiales cutáneas.

La extensión a várices esofágicas con hemorragia es mecanísticamente directa: el mismo proceso de destrucción endotelial y trombosis local aplica independientemente de si la vena es superficial (dérmico-subcutánea) o interna (submucosa esofágica). La diferencia radica únicamente en la vía de administración —endoscópica en lugar de percutánea— y en la concentración utilizada. Desde los años 1980-1990, Polidocanol fue uno de los agentes esclerosantes de referencia para la terapia endoscópica de várices esofágicas en Europa y Asia, con múltiples ECAs que confirman su eficacia en hemostasia aguda y prevención de resangrado.

Si bien la ligadura endoscópica de bandas (EVL) ha desplazado a la escleroterapia como primera línea en las guías modernas, Polidocanol mantiene relevancia clínica como opción en contextos donde EVL no está disponible, como agente complementario, o en poblaciones pediátricas con anatomía endoscópica más estrecha. La revisión basada en evidencia publicada en 2017 (PMID 29473522) documenta explícitamente estas aplicaciones off-label como una extensión lógica del mecanismo esclerosante aprobado.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00161915](https://clinicaltrials.gov/study/NCT00161915) | Fase 3 | Completado | N/A | Comparación directa de escleroterapia con Fibrin Sealant vs. ligadura con/sin **Polidocanol** para hemostasia en várices esofágicas hemorrágicas; éxito definido como supervivencia a 7 días sin sangrado clínicamente significativo. Único ensayo Fase 3 del conjunto; establece la base de evidencia L2. |
| [NCT02361593](https://clinicaltrials.gov/study/NCT02361593) | N/A | Completado | 120 | Escleroterapia endoscópica asistida por capuchón transparente con inyección de **Lauromacrogol (Polidocanol)** para el manejo de várices esofágicas; ECA con muestra adecuada que evalúa eficacia y seguridad. Ensayo de máxima relevancia directa al fármaco. |
| [NCT02468167](https://clinicaltrials.gov/study/NCT02468167) | N/A | Desconocido | 70 | Comparación de inyección endoscópica de cianoacrilato vs. BRTO (obliteración tranvenosa retrógrada con balón) en sangrado gástrico agudo por várices; proporciona contexto comparativo para la clase de escleroterapia endoscópica. |
| [NCT01923064](https://clinicaltrials.gov/study/NCT01923064) | N/A | Completado | 96 | Comparación de cianoacrilato+lipiodol vs. cianoacrilato+**Lauromacrogol** en várices gástricas; datos de seguridad para la combinación con Polidocanol en aplicación endoscópica. |
| [NCT05500625](https://clinicaltrials.gov/study/NCT05500625) | N/A | Desconocido | 70 | Coil guiado por ultrasonido endoscópico con inyección de cianoacrilato vs. BRTO en várices gástricas; técnica emergente de escleroterapia para contexto de referencia comparativa. |
| [NCT02468180](https://clinicaltrials.gov/study/NCT02468180) | N/A | Desconocido | 70 | Profilaxis primaria de sangrado por várices gástricas: inyección de cianoacrilato vs. BRTO; contexto de prevención primaria con esclerosantes. |
| [NCT02468206](https://clinicaltrials.gov/study/NCT02468206) | N/A | Completado | 64 | Prevención de resangrado por várices gástricas: cianoacrilato vs. BRTO; evalúa supervivencia a largo plazo en la misma clase terapéutica. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9255525](https://pubmed.ncbi.nlm.nih.gov/9255525/) | 1997 | ECA | *Endoscopy* | Estudio prospectivo de **cianoacrilato + Polidocanol vs. Polidocanol solo** en emergencia y tratamiento electivo de várices esofágicas en pacientes con cirrosis; establece eficacia de Polidocanol como monoterapia esclerosante. |
| [29473522](https://pubmed.ncbi.nlm.nih.gov/29473522/) | 2017 | Revisión basada en evidencia | *Current Clinical Pharmacology* | Revisión sistemática de los usos off-label de Polidocanol; documenta explícitamente la aplicación en várices esofágicas y otras localizaciones internas como extensión biológicamente coherente de su mecanismo aprobado. |
| [9514542](https://pubmed.ncbi.nlm.nih.gov/9514542/) | 1998 | ECA | *Journal of Hepatology* | **Fibrina vs. Polidocanol** como agentes de escleroterapia endoscópica para prevenir resangrado esofágico precoz; comparación directa de eficacia y perfil de complicaciones locales/sistémicas. |
| [35879573](https://pubmed.ncbi.nlm.nih.gov/35879573/) | 2022 | ECA prospectivo | *Surgical Endoscopy* | Nueva tecnología bc-EIS (escleroterapia asistida por compresión con balón) vs. EVL para erradicación de várices esofágicas; evalúa tasas de erradicación y complicaciones con agentes esclerosantes de nueva generación. |
| [36509625](https://pubmed.ncbi.nlm.nih.gov/36509625/) | 2023 | Cohorte | *Archives de Pédiatrie* | **Escleroterapia con Polidocanol** para várices cardíacas en niños y adolescentes; EIS paravaricial como alternativa a EVL con menor riesgo de resangrado por caída temprana del O-ring; uso directo en población pediátrica. |
| [32517718](https://pubmed.ncbi.nlm.nih.gov/32517718/) | 2020 | Revisión sistemática | *BMC Gastroenterology* | Análisis agrupado del riesgo de resangrado gastroesofágico tras tratamiento inicial con cianoacrilato; establece tasas de referencia históricas para comparación con esclerosantes. |
| [3069543](https://pubmed.ncbi.nlm.nih.gov/3069543/) | 1988 | Comparativo prospectivo | *Gastroenterologie Clinique et Biologique* | **Polidocanol intravariceal vs. quinina-urea perivariceal** en 74 pacientes cirróticos con sangrado esofágico; análisis de factores predictivos de resultado clínico. |
| [6609102](https://pubmed.ncbi.nlm.nih.gov/6609102/) | 1984 | Serie de casos (seguridad) | *Gut* | 34 pacientes con inyecciones paravenosas de **Polidocanol 3%** seguidos 3-47 meses; 59% desarrollaron estenosis o disfagia esofágica; dato clave de seguridad para monitoreo a largo plazo. |
| [2358974](https://pubmed.ncbi.nlm.nih.gov/2358974/) | 1990 | Serie de casos | *J Pediatr Gastroenterol Nutr* | 30 niños (7 meses–13 años) con várices esofágicas hemorrágicas tratados con escleroterapia endoscópica usando **etoxisclerol (Polidocanol)** e alcohol absoluto; 73.3% con obstrucción venosa portal extrahepática; contexto pediátrico. |
| [1778718](https://pubmed.ncbi.nlm.nih.gov/1778718/) | 1991 | Serie de casos (seguridad) | *International Surgery* | 457 pacientes japoneses con cirrosis; 6% presentaron sangrado GI alto tras escleroterapia endoscópica inicial; identifica hemorragia gástrica post-EIS (gastritis, várices gástricas, úlcera gástrica) como complicación potencialmente fatal. |

---

## Información de Mercado en Colombia

Polidocanol **no cuenta con ningún registro sanitario activo en Colombia**. El medicamento no se encuentra comercializado en el país en ninguna presentación o vía de administración.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota de brecha de datos:** No se dispone de información sobre advertencias clave, contraindicaciones ni interacciones farmacológicas en la fuente consultada. Se recomienda revisar la ficha técnica del fabricante antes de cualquier uso clínico.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Polidocanol posee un mecanismo de acción directamente aplicable a las várices esofágicas —la esclerosis vascular por destrucción endotelial es la misma independientemente de la vía de administración— y cuenta con un ensayo de Fase 3 completado (NCT00161915) y múltiples ECAs históricos que confirman su eficacia como agente esclerosante endoscópico. Sin embargo, el medicamento no está comercializado en Colombia, la escleroterapia ha sido parcialmente desplazada por EVL en las guías contemporáneas, y existen brechas de datos críticas en seguridad que deben subsanarse antes de avanzar.

**Para avanzar se necesita:**
- Gestionar el registro sanitario INVIMA para Polidocanol en formulación inyectable para uso endoscópico (concentraciones terapéuticas del 1–3%)
- Obtener y revisar el prospecto completo del fabricante: contraindicaciones, advertencias de caja negra, e interacciones farmacológicas
- Revisar las guías clínicas colombianas y latinoamericanas sobre manejo de hemorragia variceal para posicionar el rol de la escleroterapia frente a EVL como estándar local
- Evaluar la cadena de suministro regional: disponibilidad de presentaciones endoscópicas en mercados vecinos (Brasil, México, Argentina)
- Considerar un estudio comparativo local vs. EVL si se busca posicionamiento formal en guías nacionales, especialmente en centros sin acceso a ligadores endoscópicos
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

