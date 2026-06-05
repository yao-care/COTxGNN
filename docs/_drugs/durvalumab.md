---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: De Carcinoma Urotelial de Vejiga a Carcinoma Urotelial de Uretra Prostática

## Resumen en Una Frase

Durvalumab es un anticuerpo monoclonal inhibidor de PD-L1, aprobado globalmente para el carcinoma urotelial de vejiga músculo-invasivo, carcinoma pulmonar de células no pequeñas en estadio III irresecable y carcinoma hepatobiliar, entre otros tumores sólidos. El modelo TxGNN predice que podría ser efectivo para el **Carcinoma Urotelial de Uretra Prostática**, aunque actualmente **no existen ensayos clínicos ni publicaciones** específicas para esta indicación; la racionalidad se sustenta exclusivamente en el efecto de clase urotelial y la biología compartida del PD-L1.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Carcinoma urotelial de vejiga (aprobación global; sin registro en Colombia) |
| Nueva Indicación Predicha | Carcinoma urotelial de uretra prostática |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Durvalumab es un anticuerpo monoclonal humano de tipo IgG1 kappa que actúa como inhibidor del ligando de muerte programada 1 (PD-L1). Al bloquear la unión de PD-L1 con sus receptores PD-1 y CD80 (B7.1), Durvalumab restaura la capacidad citotóxica de los linfocitos T infiltrantes de tumor, revirtiendo el mecanismo de escape inmunológico que caracteriza a los carcinomas uroteliales. Aunque los datos de mecanismo de acción no están disponibles en el JSON de entrada, este perfil está bien documentado en la literatura internacional y justifica la predicción del modelo.

El carcinoma urotelial de uretra prostática comparte con el carcinoma urotelial vesical la misma estirpe histológica (células de transición), el mismo patrón de expresión elevada de PD-L1 y mecanismos equivalentes de supresión inmunológica mediada por el eje PD-1/PD-L1. La uretra prostática es una extensión anatómica directa del tracto urinario inferior, por lo que las células tumorales en este sitio presentan características moleculares prácticamente idénticas a las del carcinoma urotelial vesical, indicación para la que Durvalumab ya cuenta con aprobación regulatoria global.

El concepto de efecto de clase (class effect) en inhibidores de PD-L1 para tumores uroteliales, independientemente del sitio anatómico de origen, constituye la base teórica de esta predicción. Sin embargo, la uretra prostática como localización anatómica específica carece por completo de datos clínicos o traslacionales independientes, lo que limita la certeza al nivel mecanístico-preclínico y obliga a una postura de espera activa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación específica.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación específica.

---

## Información de Mercado en Colombia

Durvalumab no cuenta con registros sanitarios vigentes ante el INVIMA. El fármaco no está comercializado en Colombia y no se encontraron licencias registradas en la base de datos consultada (búsqueda realizada el 2026-03-29, resultado: 0 registros).

---

## Citotoxicidad

Durvalumab es un fármaco antineoplásico de la categoría inmunoterapia oncológica (inhibidor de punto de control inmunitario).

| Item | Contenido |
|------|-----------|
| Clasificación de Citotoxicidad | Inmunoterapia — Inhibidor de PD-L1 (anticuerpo monoclonal IgG1 kappa; no citotóxico convencional) |
| Riesgo de Mielosupresión | Bajo directo — no causa aplasia medular; riesgo de citopenias autoinmunes (anemia hemolítica, trombocitopenia inmune) infrecuente pero documentado |
| Clasificación de Emetogenicidad | Mínima — los anticuerpos monoclonales administrados por vía intravenosa presentan potencial emetogénico mínimo según clasificación ASCO/MASCC |
| Items de Monitoreo | Hemograma con diferencial, ALT/AST/bilirrubina (hepatitis inmuno-mediada), TSH/T4 libre (tiroiditis), glucemia en ayunas (diabetes tipo 1 inmuno-mediada), creatinina (nefritis), radiografía/TC tórax (neumonitis) |
| Protección en Manejo | Precauciones estándar para biológicos IV; no requiere las precauciones de citotóxico convencional (sin riesgo mutagénico/teratogénico por exposición cutánea a derrames) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad completa (advertencias, contraindicaciones e interacciones farmacológicas no disponibles en esta versión del Evidence Pack).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Si bien la racionalidad mecanística es coherente —el efecto de clase PD-L1 en carcinoma urotelial es biológicamente sólido—, la ausencia total de datos clínicos específicos para la uretra prostática como sitio anatómico independiente impide avanzar hacia evaluación clínica o regulatoria en este momento.

**Para avanzar se necesita:**
- Identificar series de casos o estudios retrospectivos de carcinoma urotelial de uretra prostática tratado con inhibidores de PD-L1/PD-1
- Obtener datos de expresión de PD-L1 (por inmunohistoquímica, 22C3 o SP142) específicos para tumores uroteliales de uretra prostática
- Completar la ficha de seguridad de Durvalumab con el prospecto oficial (advertencias de reacciones inmuno-mediadas, contraindicaciones y potenciales interacciones)
- Evaluar viabilidad de acceso en Colombia mediante importación especial o programa de uso compasivo, dado el estado de no comercialización ante el INVIMA
- Considerar reclasificar la prioridad de investigación hacia las indicaciones de mayor evidencia del mismo Evidence Pack (p. ej., carcinoma urotelial vesical sarcomatoide variante infiltrante, Rank 3, con recomendación "Proceed with Guardrails")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

