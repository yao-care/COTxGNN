---
layout: default
title: Alteplase
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 9
---

# Alteplase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# ALTEPLASE: Evaluación de Reposicionamiento — Sin Predicciones Disponibles

## Resumen en Una Frase

ALTEPLASE (DB00009) es un fármaco registrado en DrugBank cuya indicación original y mecanismo de acción no están disponibles en el Evidence Pack actual. El modelo TxGNN **no generó indicaciones predichas** para este candidato en la iteración presente, lo que impide realizar una evaluación de reposicionamiento completa. Se requiere completar los datos faltantes antes de poder continuar con el análisis.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos disponibles |
| Nueva Indicación Predicha | Sin predicciones generadas |
| Puntaje de Predicción TxGNN | No disponible |
| Nivel de Evidencia | — (evaluación no aplicable) |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por Qué No Hay Predicción Disponible?

El pipeline TxGNN no generó indicaciones predichas para ALTEPLASE en esta ejecución. Existen tres factores que probablemente contribuyeron a este resultado:

**Primero**, los campos de indicación original (`original_indications`) y mecanismo de acción (`original_moa`) están vacíos en el Evidence Pack. El modelo TxGNN depende del grafo de conocimiento farmacológico para establecer relaciones entre el fármaco y nuevas indicaciones; sin esta información de entrada, el modelo no puede trazar conexiones mecanísticas significativas.

**Segundo**, todo el perfil de seguridad —advertencias clave, contraindicaciones e interacciones farmacológicas— está ausente. La ausencia de datos de seguridad impide completar el nodo del fármaco en el grafo, reduciendo la densidad de conexiones disponibles para la predicción.

**Tercero**, ALTEPLASE no cuenta con registros sanitarios activos en Colombia (0 licencias), lo que elimina la señal regulatoria local que normalmente complementa la predicción del modelo.

---

## Información de Mercado en Colombia

ALTEPLASE no cuenta con registros sanitarios activos en Colombia según los datos consultados. No hay licencias vigentes registradas en la base de datos de INVIMA para este principio activo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La ausencia total de predicciones TxGNN y la insuficiencia de datos fundamentales (indicación original, mecanismo de acción, perfil de seguridad) hacen imposible emitir una recomendación de reposicionamiento en esta etapa.

**Para avanzar se necesita:**

- [ ] **MOA y indicaciones originales**: Consultar DrugBank API (`DB00009`) para obtener mecanismo de acción, categorías farmacológicas e indicaciones aprobadas
- [ ] **Advertencias y contraindicaciones**: Descargar y analizar el prospecto oficial desde TFDA o INVIMA para completar el perfil de seguridad
- [ ] **Interacciones farmacológicas**: Realizar consulta DDI con datos completos del fármaco una vez disponibles los campos básicos
- [ ] **Re-ejecución del pipeline TxGNN**: Con los datos completos, volver a ejecutar la predicción para generar indicaciones candidatas de reposicionamiento
- [ ] **Verificación regulatoria**: Confirmar estado actual en INVIMA Colombia con denominación común internacional y posibles sinónimos comerciales
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

