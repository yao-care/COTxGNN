---
layout: default
title: Turoctocog Alfa Pegol
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa Pegol
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

# Turoctocog Alfa Pegol: De Hemofilia A a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Turoctocog alfa pegol es un Factor VIII recombinante pegilado (rFVIII-PEG), diseñado para la prevención y tratamiento de hemorragias en pacientes con hemofilia A (deficiencia congénita del Factor VIII).
El modelo TxGNN predice que podría ser efectivo para el **trastorno primario de liberación plaquetaria**, sin embargo **no existen ensayos clínicos ni publicaciones** que respalden actualmente esta dirección.
La evidencia disponible se limita únicamente a la predicción computacional, lo que sitúa esta indicación en nivel L5.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Hemofilia A (deficiencia congénita del Factor VIII) |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, turoctocog alfa pegol es un Factor VIII recombinante con pegilación en el sitio O-glucosilado del dominio B (clase: terapia de reemplazo de factor de coagulación). Su eficacia en hemofilia A está comprobada: actúa como cofactor en el complejo Xase (FIXa–FVIIIa) para amplificar exponencialmente la generación de trombina durante la fase de coagulación secundaria. La pegilación extiende su vida media a aproximadamente 19 horas, lo que permite una dosificación profiláctica menos frecuente.

El trastorno primario de liberación plaquetaria (defecto en la secreción de gránulos δ y/o α) afecta la hemostasia primaria: la activación y amplificación plaquetaria inicial tras la adhesión al subendotelio. El Factor VIII, en cambio, opera en la hemostasia secundaria. Existe un punto de cruce biológico: la trombina generada por el complejo Xase puede retroactivar plaquetas vía receptores PAR-1/PAR-4, pero esta relación es indirecta, mediada por múltiples pasos y no constituye una corrección causal del defecto de liberación granular subyacente.

En consecuencia, la conexión mecanística entre rFVIII-PEG y el trastorno primario de liberación plaquetaria es débil. El elevado puntaje TxGNN probablemente refleja la proximidad de nodos de enfermedades hemorrágicas en el grafo de conocimiento (Knowledge Graph), más que una relación farmacológica directa. En el mismo perfil de predicción existen indicaciones con mayor justificación mecanística —notablemente la pseudo-enfermedad de von Willebrand (Rank 2) y la deficiencia adquirida de factores de coagulación (Rank 4)— que representan oportunidades de reposicionamiento más sólidas.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
A pesar del puntaje TxGNN de 99.997%, la conexión mecanística entre el Factor VIII recombinante pegilado y el trastorno primario de liberación plaquetaria es indirecta y carece por completo de respaldo en ensayos clínicos o literatura publicada. La indicación se clasifica en L5 (solo predicción computacional), y el análisis de racionalidad mecanística no identifica una relación causal directa que justifique avanzar a evaluación de seguridad.

**Para avanzar se necesita:**
- Confirmar el mecanismo de acción (MOA) completo mediante consulta de DrugBank API (DG002)
- Obtener las advertencias y contraindicaciones del prospecto oficial (DG001)
- Reclasificar como indicación prioritaria la **pseudo-enfermedad de von Willebrand** (Rank 2, puntuación 99.996%, mecanismo más coherente: descenso secundario de FVIII por pérdida del complejo vWF–FVIII) o la **deficiencia adquirida de factores de coagulación** (Rank 4, puntuación 99.974%, alineación directa con el efecto de clase del rFVIII)
- Búsqueda bibliográfica ampliada sobre uso de FVIII en trastornos hemorrágicos plaquetarios raros (no restringida al fármaco específico)
- Gestión de registro ante INVIMA si se decide avanzar con la indicación mejor soportada mecanísticamente
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

