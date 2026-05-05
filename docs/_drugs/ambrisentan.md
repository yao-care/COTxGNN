---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: Evaluación de Reposicionamiento – Datos Insuficientes para Predicción

## Resumen en Una Frase

Ambrisentan es un antagonista del receptor de endotelina (ERA) registrado internacionalmente para el tratamiento de la hipertensión arterial pulmonar. El Evidence Pack actual **no contiene indicaciones originales ni predicciones TxGNN**, lo que impide completar la evaluación de reposicionamiento; se requiere re-ejecución del pipeline con los datos faltantes antes de poder emitir una recomendación fundamentada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos en el Evidence Pack |
| Nueva Indicación Predicha | Sin predicciones disponibles |
| Puntaje de Predicción TxGNN | N/D |
| Nivel de Evidencia | L5 – solo predicción del modelo, sin estudios reales en el pack |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## Brechas Críticas que Bloquean la Evaluación

El Evidence Pack recibido presenta cuatro brechas que impiden completar el análisis:

**1. Sin indicaciones originales registradas** (`original_indications: []`): Las consultas al sistema regulatorio colombiano (INVIMA) no retornaron indicaciones aprobadas localmente. Sin este punto de partida, no es posible establecer la relación mecanística entre la indicación de origen y una nueva candidata.

**2. Sin predicciones TxGNN** (`predicted_indications: []`): El modelo no generó ningún candidato de reposicionamiento. Esto probablemente se debe a la ausencia del MOA y de las indicaciones originales como entradas al grafo de conocimiento.

**3. Mecanismo de acción no disponible** (`original_moa`): Este dato es el insumo principal para el análisis de relevancia mecanística. Sin él, no se puede argumentar por qué una nueva indicación sería biológicamente plausible.

**4. Datos de seguridad ausentes**: Las advertencias clave y contraindicaciones no fueron recuperadas del prospecto oficial (consulta TFDA/INVIMA pendiente de procesamiento).

> **Nota contextual (fuera del Evidence Pack):** En la literatura farmacológica general, Ambrisentan (DB06403) es conocido como antagonista selectivo del receptor ETA de endotelina, aprobado por FDA (Letairis®) y EMA (Volibris®) para hipertensión arterial pulmonar Clase II-III. Sin embargo, estos datos **no provienen del Evidence Pack actual** y no deben usarse formalmente hasta que sean validados por las fuentes primarias definidas en el protocolo.

---

## Información de Mercado en Colombia

Ambrisentan **no cuenta con registros sanitarios activos en Colombia**. La consulta al sistema regulatorio colombiano realizada el 2026-03-29 devolvió cero resultados. No existe ninguna licencia vigente para este fármaco en el país.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack carece de los datos mínimos requeridos para ejecutar la evaluación: sin indicaciones originales, sin predicciones TxGNN y sin perfil de seguridad, cualquier recomendación resultaría infundada. El pipeline debe completarse antes de retomar este candidato.

**Para avanzar se necesita:**
- **DG002 (Alta):** Consultar DrugBank API para obtener el MOA y las indicaciones aprobadas de Ambrisentan
- **DG001 (Bloqueante):** Descargar y parsear el prospecto oficial (TFDA/FDA) para extraer advertencias y contraindicaciones
- **Re-ejecución del pipeline TxGNN:** Una vez completados DG001 y DG002, re-ejecutar el modelo para generar predicciones de nuevas indicaciones
- **Consulta INVIMA expandida:** Verificar si existen registros de combinaciones o presentaciones equivalentes que contengan Ambrisentan en el mercado colombiano
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

