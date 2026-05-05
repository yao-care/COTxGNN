---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 1
---

# Aflibercept
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Usando `txgnn-pipeline` para verificar el contexto del proyecto. Ahora procedo a generar el informe de evaluación con base en el Evidence Pack provisto.

---

# Aflibercept: De Neovascularización Ocular a Esotropia

## Resumen en Una Frase

Aflibercept es una proteína de fusión recombinante que actúa como receptor señuelo (decoy receptor) para VEGF-A, VEGF-B y PlGF, originalmente empleado en el tratamiento de condiciones neovasculares oculares y oncológicas.
El modelo TxGNN predice que podría ser efectivo para **Esotropia** (estrabismo convergente),
con **0 ensayos clínicos** y **0 publicaciones** que actualmente respaldan esta dirección. La predicción carece de sustento mecanístico directo y enfrenta una paradoja clínica documentada.

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | Sin registro en Colombia (0 licencias INVIMA) |
| Nueva Indicación Predicha | Esotropia |
| Puntaje de Predicción TxGNN | 99.38% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Aflibercept es una proteína de fusión recombinante (VEGF Trap) que actúa como receptor señuelo competitivo para VEGF-A, VEGF-B y el factor de crecimiento placentario (PlGF), inhibiendo la angiogénesis patológica. Se utiliza clínicamente en degeneración macular neovascular relacionada con la edad (DMRE húmeda), edema macular diabético y retinopatía del prematuro (ROP); en su variante oncológica (ziv-aflibercept/Zaltrap) se emplea en cáncer colorrectal metastásico.

La conexión con esotropia parece haberse generado a través de una ruta indirecta en el grafo de conocimiento: **Aflibercept → ROP → Esotropia**. Esta inferencia, sin embargo, enfrenta una **paradoja direccional crítica**: el tratamiento anti-VEGF de la ROP suprime la vascularización periférica retiniana y, según la literatura disponible, puede *inducir* estrabismo —incluida la esotropia— como efecto adverso, no como resultado terapéutico. La asociación capturada por el modelo refleja, por tanto, una señal de toxicidad conocida, no una relación de eficacia.

No existe evidencia mecanística que sustente que la inhibición del VEGF pueda corregir la coordinación del movimiento ocular extrínseco ni el tono muscular para revertir la esotropia. El alto puntaje de TxGNN (99.38%) probablemente refleja correlación estructural en el grafo, no causalidad terapéutica, y debe interpretarse con precaución ante la ausencia total de evidencia clínica y preclínica de soporte.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Aflibercept no cuenta con ningún registro sanitario activo en Colombia. El fármaco no está comercializado en ninguna presentación en el país según los datos disponibles al corte de este informe.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN descansa exclusivamente en patrones del grafo de conocimiento (nivel L5, sin evidencia clínica ni preclínica), y el análisis mecanístico identifica una paradoja direccional: la inhibición del VEGF está documentada como causa de esotropia en contextos de ROP tratada, no como tratamiento de dicha condición.

**Para avanzar se necesita:**
- Obtener el MOA completo desde DrugBank o la ficha técnica EMA/FDA y verificar si existe algún vínculo plausible con la motilidad ocular extrínseca
- Revisar la lógica de inferencia del grafo de conocimiento para determinar si la ruta "Aflibercept → ROP → Esotropia" está etiquetada correctamente como relación terapéutica o como señal adversa
- Realizar búsqueda bibliográfica ampliada en oftalmología sobre mecanismos VEGF-dependientes en esotropia no neovascular
- Completar los datos de seguridad (advertencias, contraindicaciones, DDI) desde la ficha técnica oficial para habilitar la evaluación S1 de seguridad, actualmente bloqueada (DG001)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

