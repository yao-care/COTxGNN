---
layout: default
title: Caplacizumab
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Caplacizumab
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

Usando el sistema de prompt de evaluación de reposicionamiento para generar el informe a partir del Evidence Pack proporcionado.

---

# Caplacizumab: De Fármaco Sin Registro en Colombia a Tratamiento de la Púrpura Trombocitopénica Trombótica

## Resumen en Una Frase

Caplacizumab es un nanobody anti-vWF humanizado bivalente que inhibe la interacción entre los multímeros del factor von Willebrand (vWF) y las plaquetas, aprobado en Estados Unidos (2019) y Europa (2018) para el tratamiento de la púrpura trombocitopénica trombótica (PTT) adquirida, aunque actualmente no cuenta con registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para la **Púrpura Trombocitopénica Trombótica**, con **14 ensayos clínicos** y **20 publicaciones** que respaldan esta indicación.
La evidencia disponible es de Nivel L1, sustentada en los ensayos pivotales TITAN (Fase 2) y HERCULES (Fase 3) y en múltiples guías clínicas internacionales.

---

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | No registrado localmente (aprobado globalmente para PTT adquirida) |
| Nueva Indicación Predicha | Púrpura trombocitopénica trombótica (PTT) |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Caplacizumab es un fragmento de inmunoglobulina de dominio variable único (nanobody) humanizado y bivalente que actúa bloqueando de manera específica el **dominio A1 del factor von Willebrand (vWF)**. Al unirse a este dominio, impide físicamente la adhesión de los multímeros ultra-largos de vWF (UL-vWF) al receptor GPIb de la superficie plaquetaria, interrumpiendo así la cascada de adhesión plaquetaria patológica y la formación de microtrombos. Aunque el campo de mecanismo de acción estructurado no está disponible en la base de datos local consultada, este modo de acción está extensamente documentado en la literatura clínica de los ensayos TITAN y HERCULES.

La PTT adquirida es una microangiopatía trombótica causada por la deficiencia severa de ADAMTS13, la proteasa plasmática específica que normalmente escinde los UL-vWF. Sin ADAMTS13 funcional, los UL-vWF se acumulan en la circulación y se adhieren masivamente a las plaquetas a través de GPIb, generando microtrombos diseminados en la microcirculación que producen la tríada clásica: anemia hemolítica microangiopática, trombocitopenia grave y daño isquémico de órganos (cerebro, riñones, corazón). Sin tratamiento, la mortalidad supera el 90%.

Dado que el mecanismo de caplacizumab actúa directamente sobre el punto fisiopatológico central de la PTT —la unión UL-vWF/GPIb—, la predicción del modelo TxGNN no representa un reposicionamiento en sentido estricto, sino la **confirmación computacional de la indicación aprobada globalmente** que aún no cuenta con registro local. Cabe destacar que, aunque la indicación de mayor TxGNN score en el modelo es "trastorno primario de liberación plaquetaria" (Rango 1, L5), la PTT (Rango 5) es la indicación con mayor solidez clínica: sus 14 ensayos y 20 publicaciones, incluyendo ensayos Fase 3 completados y guías ISTH, constituyen la base de evidencia más robusta del conjunto.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01151423](https://clinicaltrials.gov/study/NCT01151423) | Fase 2 | Completado | 75 | TITAN: ECA simple ciego, aleatorizado, placebo-controlado; caplacizumab como terapia adyuvante al intercambio plasmático en aTTP demostró recuperación plaquetaria más rápida y reducción de exacerbaciones vs. placebo |
| [NCT02553317](https://clinicaltrials.gov/study/NCT02553317) | Fase 3 | Completado | 145 | HERCULES: ECA doble ciego, aleatorizado, placebo-controlado; evaluó eficacia de caplacizumab en restauración del recuento plaquetario y prevención de trombosis microvascular adicional en aTTP |
| [NCT05468320](https://clinicaltrials.gov/study/NCT05468320) | Fase 3 | Completado | 51 | Estudio Fase 3, abierto, un solo brazo; evaluó caplacizumab + inmunosupresión sin intercambio plasmático de primera línea en iTTP; punto primario: remisión a 24 semanas |
| [NCT02878603](https://clinicaltrials.gov/study/NCT02878603) | Fase 3 | Completado | 104 | Post-HERCULES: seguimiento prospectivo a largo plazo de seguridad, eficacia y uso repetido de caplacizumab en aTTP |
| [NCT04074187](https://clinicaltrials.gov/study/NCT04074187) | Fase 2/3 | Completado | 21 | Estudio puente japonés en aTTP adquirida; confirmó consistencia de eficacia y seguridad en población asiática, apoyando la aprobación regulatoria en Japón |
| [NCT05876221](https://clinicaltrials.gov/study/NCT05876221) | N/A | Completado | 223 | Estudio observacional retrospectivo de gran escala (n=223); evaluó la dinámica de respuesta plaquetaria a caplacizumab en la práctica real, complementando la validez externa de los RCT |
| [NCT05263193](https://clinicaltrials.gov/study/NCT05263193) | N/A | Completado | 4 | Recolección retrospectiva multicountry en pacientes pediátricos con iTTP tratados con caplacizumab; cubre brecha de datos en población infantil |
| [NCT06291025](https://clinicaltrials.gov/study/NCT06291025) | N/A | En curso | 131 | Estudio no-inferioridad prospectivo: caplacizumab + inmunosupresión + infusión de plasma sin intercambio plasmático terapéutico en iTTP; diseño innovador con enfoque en reducción de TPE |
| [NCT06376786](https://clinicaltrials.gov/study/NCT06376786) | N/A | En curso | 132 | ItaliTTP: registro nacional italiano prospectivo de iTTP; define historia natural, severidad y desenlaces clínicos en cohorte multicéntrica a 6 años |
| [NCT04985318](https://clinicaltrials.gov/study/NCT04985318) | N/A | En curso | 350 | REACT-2020: estudio observacional prospectivo alemán; documenta práctica real y factores predictores de actividad autoinmune persistente en iTTP |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/) | 2019 | ECA Fase 3 | N Engl J Med | HERCULES: caplacizumab redujo significativamente el tiempo hasta respuesta plaquetaria, el número de exacerbaciones y la mortalidad relacionada con aTTP frente a placebo |
| [26863353](https://pubmed.ncbi.nlm.nih.gov/26863353/) | 2016 | ECA Fase 2 | N Engl J Med | TITAN: primer ECA de caplacizumab en aTTP; demostró eficacia clínica y seguridad vs. placebo como base para el ensayo pivotal de Fase 3 |
| [32914526](https://pubmed.ncbi.nlm.nih.gov/32914526/) | 2020 | Guía Clínica | J Thromb Haemost | Guías ISTH 2020 para tratamiento de PTT; caplacizumab recomendado en combinación con intercambio plasmático e inmunosupresión |
| [40533296](https://pubmed.ncbi.nlm.nih.gov/40533296/) | 2025 | Actualización de Guía | J Thromb Haemost | Actualización enfocada ISTH 2025; incorpora nueva evidencia sobre manejo de iTTP y PTT congénita, incluyendo uso sin TPE |
| [32914582](https://pubmed.ncbi.nlm.nih.gov/32914582/) | 2020 | Guía Clínica | J Thromb Haemost | Guías ISTH 2020 para diagnóstico de PTT; algoritmos basados en medición de actividad de ADAMTS13 |
| [36053773](https://pubmed.ncbi.nlm.nih.gov/36053773/) | 2023 | Revisión sistemática | Blood Adv | Metaanálisis de caplacizumab + estándar de atención en iTTP; confirma superioridad sobre el estándar solo, integrando datos de RCT y estudios observacionales |
| [37045600](https://pubmed.ncbi.nlm.nih.gov/37045600/) | 2023 | Revisión sistemática | Expert Rev Hematol | Revisión sistemática y metaanálisis sobre eficacia y seguridad de caplacizumab en PTT, con análisis por subpoblaciones |
| [40235949](https://pubmed.ncbi.nlm.nih.gov/40235949/) | 2025 | Cohorte multicéntrica | EClinicalMedicine | Capla 1000+: cohorte retrospectiva internacional (>1000 pacientes); evalúa impacto de caplacizumab en mortalidad real y momento óptimo de inicio |
| [34266669](https://pubmed.ncbi.nlm.nih.gov/34266669/) | 2022 | Consenso de expertos | Med Clin | Recomendaciones españolas para diagnóstico y tratamiento de PTT; incluye caplacizumab como estándar de atención |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Revisión | J Clin Med | Revisión integral de fisiopatología, diagnóstico y manejo de PTT; contextualiza el rol de ADAMTS13, vWF y caplacizumab |

---

## Información de Mercado en Colombia

Caplacizumab **no cuenta con registro sanitario en Colombia** y no existen licencias registradas localmente. El medicamento se comercializa internacionalmente bajo el nombre **Cablivi®** (Sanofi/Ablynx), con las siguientes aprobaciones vigentes:

- **FDA (EE.UU.):** Aprobado en febrero de 2019 para adultos con PTT adquirida, en combinación con intercambio plasmático e inmunosupresión.
- **EMA (Europa):** Aprobado en septiembre de 2018 para adultos con PTT adquirida.
- **PMDA (Japón):** Aprobado con base en el estudio puente japonés (NCT04074187).

Para su uso en Colombia, se requiere iniciar el proceso de registro sanitario ante el **INVIMA**, posiblemente por la vía de homologación de aprobaciones de autoridades de referencia (FDA/EMA).

---

## Consideraciones de Seguridad

Consultar el prospecto oficial (**Cablivi®**) para información completa de seguridad, advertencias de caja negra, contraindicaciones e interacciones farmacológicas. Los datos de seguridad estructurados no están disponibles en la base de datos local consultada (INVIMA/DDI).

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Caplacizumab cuenta con evidencia de Nivel L1 —respaldada por dos ECA pivotales (TITAN Fase 2 y HERCULES Fase 3), múltiples estudios observacionales de gran escala, metaanálisis y guías clínicas internacionales (ISTH 2020/2025)— y representa el **estándar de atención global en PTT adquirida**. La ausencia de registro en Colombia no refleja una limitación de eficacia o seguridad, sino una brecha regulatoria que puede resolverse por vía de homologación. Se recomienda avanzar con cautela dado que aún se requiere completar el expediente de seguridad local.

**Para avanzar se necesita:**
- Iniciar el proceso de registro sanitario ante el **INVIMA**, utilizando la vía de aprobación por homologación con FDA/EMA como soporte regulatorio
- Obtener y revisar el prospecto oficial completo (Cablivi®) para extraer advertencias, contraindicaciones e interacciones farmacológicas relevantes para el contexto colombiano
- Completar el campo de mecanismo de acción (MOA) en la base de datos local (DrugBank ID: DB06081)
- Evaluar la estrategia de acceso en Colombia: cadena de distribución adecuada para biológico inyectable, evaluación de inclusión en el Plan de Beneficios en Salud (PBS) o rutas de recobro/acceso excepcional
- Identificar centros de referencia en Colombia con capacidad diagnóstica para medición de actividad de ADAMTS13 y manejo especializado de PTT
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

