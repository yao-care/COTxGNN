---
layout: default
title: Alirocumab
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# ALIROCUMAB: Evaluación de Reposicionamiento — Sin Indicaciones Predichas Disponibles

## Resumen en Una Frase

ALIROCUMAB es un anticuerpo monoclonal inhibidor de PCSK9, conocido por su uso en el tratamiento de la hipercolesterolemia primaria y la reducción del riesgo cardiovascular.
En este ciclo de evaluación, el modelo TxGNN **no generó indicaciones predichas** para este compuesto,
por lo que no es posible completar un análisis de reposicionamiento en este momento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipercolesterolemia / Reducción de LDL-C |
| Nueva Indicación Predicha | Sin predicciones disponibles en este ciclo |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | N/A |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué no hay Predicciones Disponibles?

El Evidence Pack de ALIROCUMAB (DB09302) fue procesado con brechas de datos críticas que impiden la generación de predicciones:

1. **Mecanismo de acción no cargado**: El pipeline no recuperó los datos de MOA desde DrugBank en este ciclo. Sin esta información, el grafo de conocimiento (KG) no puede construir las relaciones farmacológicas necesarias para TxGNN.

2. **Indicaciones originales ausentes**: El campo `original_indications` llegó vacío, lo que elimina los nodos de anclaje requeridos por el modelo para explorar indicaciones adyacentes.

3. **Array de predicciones vacío**: Como resultado de los puntos anteriores, `predicted_indications` no contiene ninguna entrada.

Desde el punto de vista del conocimiento farmacológico de dominio, ALIROCUMAB actúa como inhibidor de PCSK9 (Proprotein Convertase Subtilisin/Kexin Type 9), un anticuerpo monoclonal completamente humano que previene la degradación de los receptores de LDL en la superficie hepática, reduciendo así los niveles plasmáticos de LDL-C entre un 40–60%. Este mecanismo tiene interés teórico de reposicionamiento en áreas como enfermedad renal crónica, inflamación sistémica o síndrome metabólico, pero sin predicciones del modelo validadas no es posible emitir una recomendación fundamentada de reposicionamiento.

---

## Información de Mercado en Colombia

ALIROCUMAB no cuenta con registros sanitarios activos ante INVIMA y no está comercializado en Colombia. No hay licencias registradas en este ciclo de consulta.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack no contiene indicaciones predichas, datos de MOA ni información de seguridad recuperable, lo que hace imposible completar el análisis de reposicionamiento. No hay base de datos suficiente para emitir ninguna recomendación clínica o regulatoria.

**Para avanzar se necesita:**
- Ejecutar nuevamente el pipeline TxGNN con los datos de MOA completos recuperados desde DrugBank (DB09302)
- Descargar e interpretar el prospecto del fabricante (Praluent® / Sanofi-Regeneron) para completar advertencias, contraindicaciones y perfil de seguridad
- Cargar las indicaciones aprobadas de referencia (FDA/EMA) como nodos de anclaje en el grafo de conocimiento
- Verificar si existe solicitud de registro pendiente ante INVIMA o programas de acceso especial en Colombia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

