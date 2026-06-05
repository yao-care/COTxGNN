---
layout: default
title: Emicizumab
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab: De Hemofilia A Congénita a Pseudo-Enfermedad de von Willebrand

## Resumen en Una Frase

Emicizumab es un anticuerpo monoclonal biespecífico aprobado globalmente para la prevención de episodios hemorrágicos en hemofilia A congénita, donde actúa como mimético del Factor VIIIa puente entre FIXa y FX en la vía intrínseca de la coagulación. El modelo TxGNN predice que podría ser efectivo para la **Pseudo-Enfermedad de von Willebrand**, aunque con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. La baja correlación mecanística entre ambas condiciones genera dudas sobre la plausibilidad biológica y requiere validación adicional antes de avanzar.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Hemofilia A congénita (referencia global; sin registro en Colombia) |
| Nueva Indicación Predicha | Pseudo-Enfermedad de von Willebrand |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Emicizumab es un anticuerpo biespecífico humanizado que actúa como sustituto funcional del Factor VIIIa activado. Su mecanismo consiste en unirse simultáneamente al Factor IXa (FIXa) y al Factor X (FX), recreando el complejo tenasa y permitiendo que la coagulación secundaria progrese incluso en ausencia funcional de Factor VIII. Este mecanismo es independiente de la presencia de inhibidores anti-FVIII, lo que constituye su principal ventaja terapéutica en hemofilia A congénita.

La pseudo-enfermedad de von Willebrand (pseudo-vWD) es, sin embargo, una condición de fisiopatología opuesta: se origina por una ganancia de función en la glicoproteína plaquetaria Ib (GPIb), cuya afinidad excesiva por el factor de von Willebrand (vWF) provoca una captación anómala de multímeros de vWF por las plaquetas, resultando en trombocitopenia y deficiencia de vWF. El problema reside en la **hemostasia primaria** (interacción plaqueta-vWF), un nivel completamente distinto al punto de acción de emicizumab.

La alta puntuación del modelo TxGNN probablemente refleja la proximidad topológica en la red de enfermedades hemorrágicas: tanto la hemofilia A como la pseudo-vWD comparten nodos del grafo biológico relacionados con la coagulación. Sin embargo, esta similitud estructural no implica eficacia terapéutica. El carácter procoagulante de emicizumab podría incluso agravar el riesgo trombótico en un contexto donde la activación plaquetaria mediada por GPIb-vWF ya se encuentra aumentada. Actualmente no existe ningún estudio preclínico ni clínico que haya explorado esta posibilidad.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Emicizumab no cuenta con registros sanitarios vigentes ante el INVIMA. El fármaco no está comercializado en Colombia y no se dispone de productos aprobados localmente para ninguna indicación.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Pese a la elevada puntuación de TxGNN (99.99%), la predicción carece de cualquier respaldo clínico o preclínico y la intersección mecanística entre emicizumab (hemostasia secundaria, vía FIXa-FX) y la pseudo-vWD (hemostasia primaria, eje GPIb-vWF) es mínima. Existe adicionalmente un riesgo teórico de seguridad: el efecto procoagulante de emicizumab podría potenciar eventos trombóticos en una condición donde la activación plaquetaria ya está exacerbada.

**Para avanzar se necesita:**
- Estudios preclínicos (modelos in vitro o animales) que exploren si la potenciación de la vía FIXa-FX puede compensar el desequilibrio hemostático de la pseudo-vWD sin generar trombosis
- Evaluación formal del perfil de seguridad trombótica de emicizumab en el contexto de hiperactivación de GPIb
- Obtención y análisis del mecanismo de acción completo (MOA) desde DrugBank, pendiente de resolución del gap DG002
- Revisión por especialistas en hemostasia y trombopatías plaquetarias para evaluar la plausibilidad clínica antes de cualquier diseño de estudio
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

