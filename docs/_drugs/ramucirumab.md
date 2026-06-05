---
layout: default
title: Ramucirumab
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
---

# Ramucirumab
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

# Ramucirumab: De Adenocarcinoma Gástrico/Gastroesofágico a Adenocarcinoma de Ligamento Uterino

## Resumen en Una Frase

Ramucirumab es un anticuerpo monoclonal anti-VEGFR2 aprobado internacionalmente para el tratamiento del adenocarcinoma gástrico o de la unión gastroesofágica, cáncer colorrectal metastásico, cáncer de pulmón no microcítico y carcinoma hepatocelular.
El modelo TxGNN predice que podría ser efectivo para **Adenocarcinoma de Ligamento Uterino (uterine ligament adenocarcinoma)**,
sin embargo, actualmente **no existen ensayos clínicos ni publicaciones** que respalden directamente esta indicación, situándose en el nivel de evidencia más incipiente (L5).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Adenocarcinoma gástrico/gastroesofágico (aprobación internacional; sin registro INVIMA en Colombia) |
| Nueva Indicación Predicha | Adenocarcinoma de Ligamento Uterino |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Ramucirumab es un anticuerpo monoclonal IgG1 humano que se une con alta afinidad al dominio extracelular del receptor VEGFR2 (receptor del factor de crecimiento endotelial vascular tipo 2), bloqueando la unión de sus ligandos principales (VEGF-A, VEGF-C, VEGF-D) e inhibiendo la señalización pro-angiogénica. Este mecanismo está validado clínicamente en múltiples tumores sólidos: adenocarcinoma gástrico/gastroesofágico (en combinación con paclitaxel o en monoterapia), cáncer colorrectal metastásico (combinado con FOLFIRI), cáncer de pulmón no microcítico (con docetaxel) y carcinoma hepatocelular (con erlotinib).

El adenocarcinoma de ligamento uterino pertenece a las neoplasias malignas que surgen del parametrio profundo y tejidos de soporte uterino. La vía VEGF/VEGFR2 desempeña un papel reconocido en la angiogénesis de tumores ginecológicos. El precedente más relevante es la aprobación de bevacizumab (anti-VEGF-A) por la FDA para cáncer de cérvix recurrente/metastásico, lo que confirma que la señalización VEGF es un blanco terapéutico activo en neoplasias uterinas y del parametrio. Ramucirumab, al actuar directamente sobre el receptor VEGFR2 en lugar del ligando circulante, podría ofrecer una inhibición angiogénica más precisa y sostenida en este contexto.

No obstante, el adenocarcinoma de ligamento uterino es un subtipo tumoral extremadamente raro, con literatura clínica prácticamente inexistente. La predicción TxGNN se sustenta en la similitud biológica de la red de conocimiento con otras neoplasias responsivas a inhibición VEGFR2, pero carece de validación clínica directa en esta entidad específica. La ausencia total de ensayos clínicos o publicaciones dirigidas a esta combinación fármaco-enfermedad refleja tanto la rareza del tumor como la etapa exploratoria de esta hipótesis de reposicionamiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Ramucirumab en adenocarcinoma de ligamento uterino.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Ramucirumab en adenocarcinoma de ligamento uterino.

---

## Información de Mercado en Colombia

Ramucirumab no cuenta con registros sanitarios INVIMA activos en Colombia. El medicamento no se encuentra comercializado en el país. Para su uso eventual en investigación clínica, sería necesario tramitar una importación por vía de uso compasivo o protocolo de investigación aprobado por el INVIMA.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — anticuerpo monoclonal anti-angiogénico (inhibidor de VEGFR2); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Bajo a moderado (neutropenia no es el mecanismo primario de toxicidad; posible leucopenia leve en combinación con quimioterapia) |
| Clasificación de Emetogenicidad | Baja (administración IV; náuseas poco frecuentes como evento de infusión) |
| Items de Monitoreo | Presión arterial (hipertensión como toxicidad frecuente), proteinuria (tira reactiva y relación proteína/creatinina en orina), hemograma completo, función hepática (AST, ALT, bilirrubina), función renal (creatinina, TFGe), vigilancia de hemorragia y eventos tromboembólicos |
| Protección en Manejo | Aplicar protocolos estándar de manejo de medicamentos antineoplásicos biotecnológicos (preparación en cabina de bioseguridad, EPP completo, descarte como residuo peligroso citotóxico) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias y contraindicaciones no están disponibles en la fuente local consultada (sin registro INVIMA). Se recomienda revisar el prospecto FDA/EMA de Cyramza® (ramucirumab) para las advertencias sobre hemorragia grave, perforación gastrointestinal, alteración de la cicatrización de heridas, hipertensión arterial y síndrome de encefalopatía posterior reversible (PRES), que son las advertencias de recuadro negro reconocidas internacionalmente para este medicamento.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La base mecanística es biológicamente plausible —inhibición VEGFR2 en tumores ginecológicos con soporte indirecto del precedente bevacizumab en cérvix—, pero el adenocarcinoma de ligamento uterino es un subtipo extremadamente raro sin ninguna evidencia clínica directa (L5), y ramucirumab carece de registro INVIMA en Colombia, lo que representa una barrera regulatoria y logística significativa para cualquier desarrollo clínico inmediato.

**Para avanzar se necesita:**
- Obtener los datos completos de mecanismo de acción (MOA) y perfil de seguridad desde DrugBank y el prospecto FDA/EMA (actualmente en Data Gap)
- Realizar búsqueda de series de casos o reportes de adenocarcinoma de ligamento uterino tratados con agentes anti-VEGF/VEGFR para establecer la base de evidencia de nivel L4
- Evaluar la expresión inmunohistoquímica de VEGFR2 en muestras de adenocarcinoma de ligamento uterino disponibles en biobancos
- Consultar con oncólogos ginecológicos especializados sobre la viabilidad epidemiológica de un protocolo de investigación (número de casos accesibles)
- Explorar la posibilidad de incluir esta indicación en un basket trial o umbrella trial existente de ramucirumab en tumores ginecológicos raros
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

