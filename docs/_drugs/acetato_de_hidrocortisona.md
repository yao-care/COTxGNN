---
layout: default
title: Acetato De Hidrocortisona
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 0
---

# Acetato De Hidrocortisona
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

# Acetato de Hidrocortisona: Evaluación Preliminar — Sin Indicaciones Predichas Disponibles

---

## Resumen en Una Frase

El Acetato de Hidrocortisona es un corticosteroide conocido, ampliamente utilizado en diversas condiciones inflamatorias, alérgicas e inmunológicas. En esta evaluación, el modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco. Además, no se identificaron registros sanitarios vigentes en Colombia ni datos de seguridad específicos en las fuentes consultadas.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No disponible en las fuentes consultadas |
| Nueva Indicación Predicha | — (Sin predicciones generadas por TxGNN) |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 — Solo evaluación preliminar, sin estudios ni predicciones |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no se Generaron Predicciones?

El Acetato de Hidrocortisona es la forma éster acetilada de la hidrocortisona, un glucocorticoide endógeno que actúa mediante la unión al receptor de glucocorticoides intracelular, modulando la transcripción génica para suprimir respuestas inflamatorias e inmunológicas. Sus indicaciones clásicas abarcan un amplio espectro: insuficiencia suprarrenal, enfermedades inflamatorias articulares, dermatosis, asma, enfermedades autoinmunes, entre otras.

La ausencia de predicciones por parte del modelo TxGNN puede deberse a múltiples factores: (1) el fármaco ya cuenta con un perfil de indicaciones extremadamente amplio, lo que reduce el espacio para reposicionamiento novedoso; (2) es posible que el identificador utilizado ("ACETATO DE HIDROCORTISONA") no haya sido mapeado correctamente al grafo de conocimiento del modelo; o (3) los datos de entrada del fármaco presentan brechas significativas (sin DrugBank ID, sin mecanismo de acción formal registrado en el pack) que impiden la ejecución del algoritmo predictivo.

Se recomienda verificar el mapeo del fármaco en el grafo de conocimiento de TxGNN utilizando el nombre DCI en inglés (*Hydrocortisone Acetate*) o el DrugBank ID correspondiente (DB01171 para hidrocortisona) antes de descartar el candidato.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en el Evidence Pack para este candidato.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en el Evidence Pack para este candidato.

---

## Información de Mercado en Colombia

No se identificaron registros sanitarios vigentes para Acetato de Hidrocortisona en las fuentes regulatorias consultadas. El estado de mercado reportado es **"No comercializado"**.

> **Nota:** Esto no implica necesariamente que la hidrocortisona (en otras sales o formas farmacéuticas) no esté disponible en el mercado colombiano. Se recomienda verificar con las bases de datos del INVIMA utilizando variantes del nombre (hidrocortisona, hidrocortisona acetato, hydrocortisone).

---

## Consideraciones de Seguridad

No se dispone de datos de seguridad específicos en las fuentes consultadas para este Evidence Pack. Consultar el prospecto del producto para información completa de seguridad.

> **Información general conocida sobre hidrocortisona:** Los corticosteroides sistémicos pueden causar supresión del eje hipotálamo-hipófiso-suprarrenal, hiperglucemia, inmunosupresión, osteoporosis, úlcera péptica, y síndrome de Cushing iatrogénico con uso prolongado. Las contraindicaciones generales incluyen infecciones fúngicas sistémicas y hipersensibilidad conocida al principio activo.

---

## Brechas de Datos Identificadas

El Evidence Pack señala las siguientes brechas críticas que deben ser resueltas:

| ID | Categoría | Dato Faltante | Severidad | Impacto | Fuente de Remediación |
|----|-----------|---------------|-----------|---------|----------------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto | **Bloqueante** | No se puede realizar la evaluación inicial de seguridad (S1) | Sitio web del ente regulador — descargar y analizar prospecto PDF |
| DG002 | Nivel de Fármaco | Mecanismo de acción (MOA) | Alta | Afecta el análisis de correlación mecanística | DrugBank — consultar API con DrugBank ID |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen predicciones de nuevas indicaciones generadas por el modelo TxGNN para este candidato, y se presentan brechas de datos bloqueantes que impiden una evaluación de seguridad adecuada. Además, el fármaco no cuenta con registros sanitarios vigentes en Colombia, lo que añade una barrera regulatoria significativa para cualquier estrategia de reposicionamiento.

**Para avanzar se necesita:**
- Resolver el mapeo del fármaco en el grafo de conocimiento de TxGNN (verificar con DrugBank ID: DB01171 y nombre en inglés *Hydrocortisone Acetate*)
- Obtener el DrugBank ID y los datos de mecanismo de acción (MOA) formales
- Obtener las advertencias, contraindicaciones y prospecto oficial del ente regulatorio colombiano (INVIMA)
- Re-ejecutar la predicción de TxGNN una vez resueltas las brechas de datos
- Evaluar si la hidrocortisona bajo otras sales o formas farmacéuticas ya comercializadas en Colombia podría ser un mejor candidato de reposicionamiento
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

