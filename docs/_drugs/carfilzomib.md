---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

El skill `txgnn-pipeline` confirma el contexto del proyecto. Procedo ahora a generar el informe de evaluación de reposicionamiento basándome en el Evidence Pack proporcionado.

---

# Carfilzomib: De Mieloma Múltiple a Melanoma Cutáneo Maligno (CMM7)

## Resumen en Una Frase

Carfilzomib es un inhibidor irreversible del proteasoma aprobado internacionalmente para el tratamiento del mieloma múltiple en recaída o refractario, aunque no cuenta con registro sanitario en Colombia. El modelo TxGNN predice que podría ser efectivo para **CMM7** (Melanoma Cutáneo Maligno tipo 7), con **0 ensayos clínicos** y **0 publicaciones** que respalden directamente esta indicación específica. La predicción se basa exclusivamente en similitud topológica del grafo de conocimiento biológico, por lo que debe interpretarse como señal exploratoria en etapa muy temprana.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | Mieloma múltiple (aprobación internacional; sin registro en Colombia) |
| Nueva Indicación Predicha | CMM7 (Melanoma Cutáneo Maligno tipo 7) |
| Puntaje de Predicción TxGNN | 99.37% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción desde las fuentes consultadas. Por su clase farmacológica conocida, Carfilzomib es un inhibidor irreversible del proteasoma 20S (subunidad β5, clase epoxicetona), que actúa acumulando proteínas mal plegadas en la célula tumoral a través de la Respuesta a Proteínas Desplegadas (Unfolded Protein Response, UPR), desencadenando apoptosis. Este mecanismo no es exclusivo del mieloma: cualquier célula tumoral con alta dependencia proteosómica puede ser vulnerable, lo que representa la base biológica general de su extrapolación a neoplasias sólidas.

CMM7 es un código de clasificación para un subtipo específico de melanoma cutáneo maligno. El puntaje TxGNN de 0.9937 se origina en la proximidad topológica que el modelo infiere entre el mecanismo de Carfilzomib y los nodos moleculares del melanoma dentro del grafo de conocimiento, sin contar con ensayos clínicos ni literatura que respalden directamente esta subclasificación. Cabe destacar que para el diagnóstico más amplio de **melanoma** (indicación relacionada, rango 5 del mismo perfil predictivo), existe evidencia preclínica preliminar en células B16-F1 (PMID 33671902, nivel L4), lo que le da sustento biológico a la familia de indicaciones melanoma, pero no al subtipo CMM7 de forma específica.

La predicción debe tratarse como hipótesis generada por IA pendiente de validación. La ausencia de estudios in vivo, de modelos de CMM7, y la falta de definición clínica estandarizada de este subtipo representan barreras importantes antes de cualquier desarrollo ulterior.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Carfilzomib en CMM7.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Carfilzomib en CMM7.

---

## Información de Mercado en Colombia

Carfilzomib no cuenta con registros sanitarios activos en Colombia (INVIMA). El fármaco no está comercializado en el mercado colombiano. Cualquier uso futuro requeriría tramitar registro sanitario ante INVIMA previo a cualquier estudio o comercialización local.

---

## Citotoxicidad

| Ítem | Contenido |
|------|-----------|
| Clasificación de Citotoxicidad | Citotóxico convencional — Inhibidor irreversible del Proteasoma (clase epoxicetona) |
| Riesgo de Mielosupresión | Alto — neutropenia, trombocitopenia y anemia son eventos adversos frecuentes documentados en su uso para mieloma múltiple |
| Clasificación de Emetogenicidad | Baja a moderada |
| Ítems de Monitoreo | Hemograma completo con diferencial, función renal y hepática, presión arterial, función cardíaca (fracción de eyección ventricular izquierda — FEVI) |
| Protección en Manejo | Debe seguir regulaciones de manejo de fármacos citotóxicos; administración intravenosa exclusivamente en entorno hospitalario controlado |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
CMM7 es un subtipo de melanoma sin ningún ensayo clínico ni publicación que respalde directamente el uso de Carfilzomib, y la puntuación TxGNN de 99.37% refleja similitud topológica en el grafo de conocimiento biológico, no evidencia clínica o preclínica real. Adicionalmente, el fármaco no está registrado en Colombia, lo que añade una barrera regulatoria significativa.

**Para avanzar se necesita:**

- Confirmar la definición clínica exacta y los criterios diagnósticos del subtipo CMM7
- Obtener datos de mecanismo de acción (MOA) completos desde DrugBank o literatura primaria
- Realizar estudios preclínicos in vitro en líneas celulares de melanoma cutáneo (punto de partida: aprovechar la evidencia existente en células B16-F1, PMID 33671902)
- Escalar a modelos in vivo antes de considerar cualquier indicación clínica
- Descargar y analizar la ficha técnica de referencia (FDA/EMA) para completar perfil de seguridad (advertencias, contraindicaciones, DDI)
- Evaluar viabilidad de registro sanitario ante INVIMA Colombia como requisito previo a cualquier desarrollo clínico local
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

