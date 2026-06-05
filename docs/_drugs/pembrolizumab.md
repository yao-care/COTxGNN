---
layout: default
title: Pembrolizumab
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
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

# Pembrolizumab: De Inmunoterapia Oncologica a Fibromatosis Gingival

## Resumen en Una Frase

Pembrolizumab es un anticuerpo monoclonal anti-PD-1 reconocido globalmente como inmunoterapia de primera y segunda linea para multiples tipos de cancer, incluyendo melanoma, cancer de pulmon no celulas pequenas (NSCLC), cancer colorrectal MSI-H y otros tumores solidos con alta expresion de PD-L1.
El modelo TxGNN predice que podria ser efectivo para **Fibromatosis Gingival**,
sin embargo, actualmente **no existen ensayos clinicos ni publicaciones** que respalden esta direccion, y la conexion biologica es biologicamente cuestionable.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No registrado en Colombia (farmaco no comercializado) |
| Nueva Indicacion Predicha | Fibromatosis Gingival |
| Puntaje de Prediccion TxGNN | 99.40% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Numero de Registros Sanitarios | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en el Evidence Pack. Sin embargo, Pembrolizumab es un anticuerpo monoclonal humanizado IgG4 dirigido contra el receptor de muerte programada 1 (PD-1). Su mecanismo consiste en bloquear la interaccion entre PD-1 y sus ligandos PD-L1/PD-L2, impidiendo la inhibicion de los linfocitos T y permitiendo que el sistema inmune reconozca y ataque celulas tumorales que expresan PD-L1. Esta es la base de sus aprobaciones en multiples tumores solidos con alta carga mutacional o alta expresion de PD-L1.

La fibromatosis gingival hereditaria es una enfermedad benigna de origen genetico, causada por mutaciones en los genes SOS1 o GINGF, que provocan proliferacion de fibroblastos gingivales sin transformacion maligna. A diferencia de los tumores solidos donde pembrolizumab ha demostrado eficacia, esta condicion no involucra mecanismos de escape inmunologico mediados por el eje PD-1/PD-L1. La expresion de PD-L1 en tejido fibromatoso benigno es tipicamente nula o insignificante, y la enfermedad carece de la carga mutacional (TMB) que suele correlacionarse con respuesta a inhibidores de punto de control.

Desde el punto de vista clinico, la relacion riesgo-beneficio es claramente desfavorable: el tratamiento estandar para la fibromatosis gingival es la gingivectomia quirurgica o el seguimiento, sin necesidad de terapia sistemica. La exposicion a pembrolizumab impondria un riesgo de eventos adversos inmunomediados (irAE) del 10-20% para una condicion no amenazante para la vida. El alto puntaje del modelo TxGNN (99.40%) probablemente refleja correlaciones estructurales en el grafo de conocimiento biologico, no una relacion terapeutica directa.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Inmunoterapia — Inhibidor de punto de control inmune (anti-PD-1); no es citotoxico convencional |
| Riesgo de Mielosupresion | Bajo (no produce mielosupresion directa; puede ocurrir anemia hemolitica autoinmune o trombocitopenia inmunomediada de forma infrecuente) |
| Clasificacion de Emetogenicidad | Muy baja |
| Items de Monitoreo | Funcion tiroidea (TSH/T4L), funcion hepatica (ALT/AST/bilirrubina), funcion renal (creatinina), cortisol basal, glucosa, hemograma completo; signos de neumonitis, colitis y dermatitis inmunomediada |
| Proteccion en Manejo | Producto biologico refrigerado (2–8 °C); no requiere las medidas de proteccion de citotoxicos convencionales (sin riesgo de citotoxicidad por contacto), pero debe manejarse bajo protocolos de oncologia para productos biologicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La fibromatosis gingival es una enfermedad benigna de origen genetico cuya fisiopatologia no involucra el eje PD-1/PD-L1 ni mecanismos de escape inmunologico tumoral. No existe ninguna evidencia clinica o preclinca que respalde el uso de pembrolizumab en esta condicion, y el perfil riesgo-beneficio es claramente desfavorable.

**Para avanzar se necesita:**
- Datos de expresion de PD-L1 y densidad de linfocitos infiltrantes en biopsias de tejido de fibromatosis gingival
- Hipotesis biologica explicita que vincule el bloqueo del eje PD-1/PD-L1 con la proliferacion de fibroblastos gingivales
- Registro sanitario de pembrolizumab ante INVIMA Colombia como prerequisito para cualquier investigacion clinica local
- Evaluacion de la decision TxGNN frente a indicaciones de mayor rango biologico plausible (por ejemplo, lung hilum carcinoma o pulmonary sulcus neoplasm, donde existen mecanismos de accion directamente aplicables y evidencia clinica indirecta de Fase 3)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

