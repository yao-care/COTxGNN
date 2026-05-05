---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

# Imiquimod: De Queratosis Actínica a Neoplasia Premaligna

## Resumen en Una Frase

Imiquimod es un modulador de respuesta inmune (agonista TLR7) aprobado por la FDA para el tratamiento de queratosis actínica, carcinoma basocelular superficial y verrugas genitales externas, aunque actualmente no cuenta con registro INVIMA en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Neoplasia Premaligna** de forma más amplia y sistemática,
con **19 ensayos clínicos** y **9 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin registro INVIMA en Colombia (referencia internacional: Queratosis Actínica, CBC superficial, Verrugas Genitales — FDA) |
| Nueva Indicación Predicha | Neoplasia Premaligna (pre-malignant neoplasm) |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No Comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Imiquimod es un agonista del receptor tipo Toll 7 (TLR7) que activa simultáneamente la inmunidad innata y adaptativa. Al unirse a TLR7 en células dendríticas plasmocitoides y macrófagos, desencadena una cascada de producción de interferón-alfa (IFN-α) y citocinas proinflamatorias (TNF-α, IL-12), induciendo la polarización hacia un perfil Th1. Este estado inmune local facilita la eliminación de células infectadas por HPV mediante activación de linfocitos T citotóxicos, y promueve la apoptosis de queratinocitos con daño acumulado por radiación ultravioleta. Adicionalmente, la activación TLR7 suprime la actividad de células T reguladoras (Treg) en el microambiente tumoral local, un mecanismo crítico para las lesiones premalignas.

Las neoplasias premalignas —incluyendo queratosis actínica (AK), neoplasia intraepitelial cervical (CIN), neoplasia intraepitelial vulvar (VIN), neoplasia intraepitelial anal (AIN) y lentigo maligno— comparten una característica farmacológicamente relevante: son lesiones superficiales, accesibles a la vía tópica, en las cuales la inmunomodulación local puede ejercer efecto terapéutico directo sin necesidad de exposición sistémica significativa. La arquitectura de estas lesiones —epitelios estratificados con infiltrado inflamatorio local— es el contexto óptimo para el mecanismo de Imiquimod.

La predicción de TxGNN resulta altamente coherente: Imiquimod ya opera dentro del espectro de neoplasia premaligna en sus indicaciones aprobadas (AK) y maligna incipiente (CBC superficial). La extensión a "neoplasia premaligna" como categoría unificada refleja la lógica mecanística del fármaco y está respaldada por ensayos clínicos en múltiples subtipos de lesiones premalignas en distintos órganos. Esto no representa un salto especulativo, sino una generalización basada en un denominador común inmunológico.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Fase 3 | Completado | 259 | Imiquimod como tratamiento neoadyuvante para reducir márgenes de escisión en Lentigo Maligno facial (melanoma intraepidérmico / pre-invasivo); mayor ECA completado directamente en neoplasia premaligna con Imiquimod |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Fase 2 | Completado | 90 | ECA aleatorizado que evalúa eficacia de imiquimod tópico en neoplasia intraepitelial cervical (CIN) de alto grado; regresión de CIN como desenlace primario |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Fase 3 | Terminado | 9 | Imiquimod tópico vs LLETZ en CIN 2-3; terminado prematuramente (n=9 de meta prevista), sin conclusiones de eficacia; señal de riesgo ejecutivo importante |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Fase 1 | Terminado | 49 | Comparación de imiquimod 5%, 0.05% y nanoencapsulado en gel para queilitis actínica (lesión premaligna del labio inferior); evaluación de concentración óptima |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Fase 1 | Completado | 16 | Imiquimod tópico (Aldara) como inmunoterapia neoadyuvante en carcinoma oral de células escamosas en estadio temprano; evalúa activación TLR7 y su efecto en microambiente tumoral de lesiones borderline premalignas/malignas |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Fase 3 | Completado | 20 | Imiquimod 5% aplicado 3 días/semana en 1 o 2 ciclos para queratosis actínicas en cabeza; evaluación de duración de respuesta y recurrencia |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Fase 4 | Desconocido | 20 | Imiquimod 3.75% combinado con crioterapia previa para queratosis actínicas hipertróficas en dorso de manos y antebrazos; abordaje de campo de cancerización |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Fase 3 | Desconocido | 145 | Ensayo de no inferioridad: escisión quirúrgica vs curetaje + imiquimod para carcinoma basocelular nodular; el mayor ensayo comparativo de imiquimod frente a cirugía estándar |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Fase 2 | Completado | 5 | Mecanismos de escape inmune en lesiones HPV-asociadas; evalúa imiquimod en VIN 2/3 y verrugas anogenitales; análisis de respuesta inmune tisular |
| [NCT01792505](https://clinicaltrials.gov/study/NCT01792505) | Fase 1 | Completado | 71 | Resección quirúrgica + vacuna de células dendríticas con imiquimod como adyuvante en glioma maligno; mayor cohorte completada con imiquimod adyuvante (n=71), provee datos de seguridad a largo plazo |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Revisión Sistemática (Cochrane) | Cochrane Database Syst Rev | Intervenciones para neoplasia intraepitelial del canal anal (AIN) HPV-asociada; identifica imiquimod como opción terapéutica con perfil de evidencia evaluado sistemáticamente |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Revisión Sistemática (Cochrane) | Cochrane Database Syst Rev | Intervenciones médicas para VIN de alto grado; posiciona imiquimod como alternativa no quirúrgica con menor morbilidad que la escisión, especialmente relevante en mujeres jóvenes |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Revisión | Int J Mol Sci | Tratamientos combinados con terapia fotodinámica para cáncer de piel no melanoma; discute el rol de imiquimod en el manejo de campo de cancerización y lesiones premalignas múltiples (AK, enfermedad de Bowen) |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Revisión | Skin Therapy Letter | Manejo actual de queratosis actínicas; posiciona imiquimod como terapia de campo para AK múltiples, con ventaja sobre crioterapia en lesiones subclínicas adyacentes |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Revisión | Semin Cutan Med Surg | Estrategias de tratamiento tópico para cáncer de piel no melanoma y lesiones premalignas; evalúa comparativamente fluorouracilo, diclofenaco, imiquimod y PDT |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Estudio Animal/PK | Urol Oncol | Farmacocinética y farmacodinámica de agonistas TLR7 (TMX-101, TMX-202) por vías intravesical e intravenosa en modelo de rata; sustenta la viabilidad del concepto de aplicación no cutánea de agonistas TLR7 en lesiones premalignas de cavidades |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Reporte de Caso | Int J STD AIDS | Tratamiento exitoso de VIN de alto grado con imiquimod 5% en receptora de trasplante renal inmunosuprimida; señal positiva de eficacia incluso en contexto de inmunosupresión farmacológica |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Reporte de Caso | Int J STD AIDS | Papulosis bowenoide del pene (condición premaligna HPV-asociada) tratada con éxito con imiquimod 5% tópico en monoterapia semanal |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Reporte de Caso/Imagen | Hautarzt | Poroqueratosis actínica superficial diseminada con múltiples lesiones premalignas en miembros inferiores (AK, CEC, enfermedad de Bowen); contexto clínico de resistencia a imiquimod en paciente compleja |

---

## Información de Mercado en Colombia

Imiquimod no cuenta con ningún registro sanitario INVIMA activo en Colombia. El fármaco no está disponible como producto registrado en el mercado colombiano a la fecha de corte del análisis (2026-05-05).

Para su uso en Colombia se requeriría tramitar importación con fines de investigación, uso compasivo, o iniciar proceso de registro ante INVIMA. En otros mercados internacionales (EE. UU., Unión Europea, Japón, entre otros) el producto se comercializa bajo las marcas Aldara y Zyclara para indicaciones dermatológicas.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunomodulador / Agonista TLR7 (no citotóxico convencional; mecanismo de acción inmune, no citostático directo) |
| Riesgo de Mielosupresión | Bajo (formulación tópica con absorción sistémica mínima; sin evidencia de mielosupresión clínicamente relevante en uso estándar) |
| Clasificación de Emetogenicidad | Mínima (uso exclusivamente tópico; sin efecto emetogénico sistémico documentado) |
| Ítems de Monitoreo | Reacciones cutáneas locales (eritema, vesiculación, erosión, costras — esperadas y dosis-dependientes); función inmune basal en pacientes inmunosuprimidos; vigilancia de lesiones tratadas para descartar progresión |
| Protección en Manejo | Evitar contacto con mucosas no diana y ojos; precaución en embarazo (Categoría C FDA); en pacientes inmunocomprometidos, monitoreo estrecho dado caso documentado de conversión maligna (PMID 12719972) |

---

## Consideraciones de Seguridad

**Señal de Seguridad Relevante:**
El PMID 12719972 documenta un caso de conversión maligna de papilomatosis oral florida durante tratamiento tópico con imiquimod en paciente inmunocomprometida. Si bien es un reporte aislado, constituye una señal que no debe ignorarse en el contexto de uso en lesiones orales o mucosas en población de riesgo.

**Interacciones Farmacológicas:**
No se identificaron interacciones farmacológicas registradas en las bases de datos consultadas (resultado: not_found, 0 interacciones).

Para información completa de advertencias, contraindicaciones y precauciones, consultar el prospecto oficial (Aldara/Zyclara) de la FDA o EMA, dado que no se dispone de ficha técnica INVIMA.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La evidencia de nivel L2 respalda el uso de Imiquimod en neoplasia premaligna, sustentada por un ECA de Fase 3 completado con 259 pacientes (lentigo maligno facial), un ECA de Fase 2 completado con 90 pacientes (CIN alto grado), dos revisiones sistemáticas Cochrane independientes (VIN y AIN), y múltiples ensayos de Fase 3 adicionales en queratosis actínica y CBC. El mecanismo TLR7→IFN-α→Th1 es farmacológicamente coherente con la totalidad del espectro de neoplasia premaligna superficial. La barrera principal para Colombia no es de eficacia sino regulatoria: la ausencia de registro INVIMA requiere una estrategia de acceso específica antes de cualquier implementación.

**Para avanzar se necesita:**

- Tramitar registro INVIMA o definir vía de acceso alternativa (importación para investigación, uso compasivo) dado que el fármaco no está disponible en Colombia
- Obtener y revisar el prospecto completo (FDA/EMA) para documentar formalmente contraindicaciones y advertencias de caja negra
- Confirmar mecanismo de acción completo mediante consulta a DrugBank API (DG002 actualmente pendiente)
- Definir la subpoblación diana prioritaria en Colombia (AK, CIN, VIN o AIN) para focalizar el plan de desarrollo clínico y la solicitud regulatoria
- Establecer protocolo de monitoreo de seguridad para poblaciones especiales (trasplantados, pacientes con VIH/SIDA, inmunocomprometidos) dada la señal de conversión maligna documentada
- Evaluar viabilidad de formulaciones alternativas (nanoencapsulado, concentraciones reducidas) si se contemplan indicaciones en mucosas no cutáneas
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

