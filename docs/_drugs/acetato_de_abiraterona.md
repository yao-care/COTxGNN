---
layout: default
title: Acetato De Abiraterona
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 0
---

# Acetato De Abiraterona
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Acetato de Abiraterona: Evaluación Preliminar — Datos Insuficientes para Reposicionamiento

---

## Resumen en Una Frase

Acetato de Abiraterona es un inhibidor de CYP17A1 ampliamente utilizado en el tratamiento del cáncer de próstata metastásico resistente a la castración (mCRPC). En esta evaluación, **no se generaron predicciones de nuevas indicaciones** por parte del modelo TxGNN, y el paquete de evidencia presenta múltiples brechas de datos críticas que impiden una evaluación completa de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No disponible en el paquete de evidencia (conocida: cáncer de próstata metastásico resistente a la castración) |
| Nueva Indicación Predicha | — Sin predicciones generadas por TxGNN — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | **L5** (sin evidencia clínica vinculada a nueva indicación) |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no se Generaron Predicciones?

Acetato de Abiraterona es un inhibidor selectivo de la enzima CYP17A1 (17α-hidroxilasa/C17,20-liasa), que bloquea la biosíntesis de andrógenos tanto a nivel suprarrenal como intratumoral. Es un fármaco antineoplásico de terapia dirigida hormonal ampliamente aprobado a nivel mundial para el tratamiento del cáncer de próstata metastásico resistente a la castración, en combinación con prednisona.

En esta evaluación, el modelo TxGNN no generó predicciones de nuevas indicaciones (`predicted_indications` vacío). Esto puede deberse a varias razones: (1) el fármaco no fue incluido en el grafo de conocimiento utilizado por TxGNN, (2) el identificador DrugBank no fue resuelto (`drugbank_id: null`), o (3) las indicaciones ya conocidas del fármaco cubren los nodos de enfermedad con mayor puntaje de predicción.

Adicionalmente, el paquete de evidencia presenta brechas de datos clasificadas como **Blocking** (advertencias/contraindicaciones regulatorias) y **High** (mecanismo de acción), lo que impide completar la evaluación de seguridad y la correlación mecanística necesarias para un análisis de reposicionamiento robusto.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con nuevas indicaciones registrados en este paquete de evidencia, dado que no se generaron predicciones de reposicionamiento.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con nuevas indicaciones disponible en este paquete de evidencia, dado que no se generaron predicciones de reposicionamiento.

---

## Información de Mercado en Colombia

Acetato de Abiraterona **no se encuentra comercializado** en Colombia según los datos regulatorios consultados. No se identificaron registros sanitarios vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------------------|---------------------|---------------------|---------------------|
| — | — | — | — |

> No se encontraron registros sanitarios para este principio activo en la base de datos consultada.

---

## Citotoxicidad

Acetato de Abiraterona es un agente antineoplásico, por lo que se incluye esta sección de evaluación.

| Item | Contenido |
|------|-----------|
| Clasificación de Citotoxicidad | **Terapia dirigida** (inhibidor de CYP17A1 — terapia hormonal antiandrógena) |
| Riesgo de Mielosupresión | Bajo (no es un citotóxico convencional; sin embargo, se han reportado casos de anemia) |
| Clasificación de Emetogenicidad | Baja |
| Ítems de Monitoreo | Presión arterial, potasio sérico, función hepática (ALT/AST), función cardíaca, niveles de cortisol, hemograma |
| Protección en Manejo | Precauciones estándar de manejo de fármacos antineoplásicos; no requiere protección de citotóxico convencional |

> **Nota:** Abiraterona se asocia con mineralocorticoidismo (hipertensión, hipocalemia, retención de líquidos) debido a la acumulación de precursores de mineralocorticoides por la inhibición de CYP17A1. El uso concomitante de prednisona mitiga estos efectos.

---

## Consideraciones de Seguridad

> ⚠️ **Brecha de datos crítica (Blocking):** No se dispone de las advertencias, contraindicaciones ni información de interacciones farmacológicas provenientes del prospecto regulatorio. Esta información es necesaria para completar la evaluación de seguridad.

Consultar el prospecto del producto para información completa de seguridad. A nivel general, las consideraciones de seguridad conocidas para abiraterona incluyen:

- **Hepatotoxicidad:** Se requiere monitoreo de función hepática antes y durante el tratamiento.
- **Mineralocorticoidismo:** Hipertensión, hipocalemia y retención de líquidos por acumulación de precursores suprarrenales.
- **Insuficiencia suprarrenal:** Riesgo en situaciones de estrés o si se interrumpe la prednisona concomitante.
- **Toxicidad cardíaca:** Se han reportado arritmias y eventos cardiovasculares.

---

## Brechas de Datos Identificadas

| ID | Categoría | Ítem Faltante | Severidad | Impacto | Fuente de Remediación |
|----|-----------|---------------|-----------|---------|----------------------|
| DG001 | Nivel de Fármaco | Advertencias/Contraindicaciones regulatorias | **Blocking** | No se puede iniciar la evaluación de seguridad S1 | Descargar y analizar prospecto PDF del ente regulatorio |
| DG002 | Nivel de Fármaco | Mecanismo de Acción (MOA) | **Alta** | Afecta el análisis de correlación mecanística | Consultar API de DrugBank |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No se generaron predicciones de nuevas indicaciones por parte del modelo TxGNN para Acetato de Abiraterona. Adicionalmente, el paquete de evidencia presenta brechas de datos clasificadas como **Blocking** que impiden completar la evaluación de seguridad. Sin predicciones ni datos de seguridad regulatorios, no es posible avanzar con una evaluación de reposicionamiento en este momento.

**Para avanzar se necesita:**
- Resolver el identificador DrugBank (`drugbank_id`) para vincular el fármaco al grafo de conocimiento de TxGNN
- Obtener el prospecto regulatorio para extraer advertencias, contraindicaciones y datos de seguridad (DG001 — Blocking)
- Completar los datos de mecanismo de acción desde DrugBank (DG002 — Alta)
- Re-ejecutar la predicción TxGNN una vez que el fármaco esté correctamente mapeado en el grafo de conocimiento
- Verificar el estado regulatorio en Colombia, dado que abiraterona está ampliamente disponible a nivel mundial (posible error de consulta con el nombre en español "ACETATO DE ABIRATERONA")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

