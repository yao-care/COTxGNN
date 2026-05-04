---
layout: default
title: Lansoprazol
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 0
---

# Lansoprazol
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

# LANSOPRAZOL: Evaluación de Reposicionamiento — Sin Predicciones Disponibles

## Resumen

LANSOPRAZOL es un inhibidor de la bomba de protones (IBP) ampliamente reconocido por su uso en enfermedades relacionadas con el ácido gástrico (úlcera péptica, ERGE, síndrome de Zollinger-Ellison). En esta evaluación, el modelo TxGNN **no generó indicaciones candidatas** para este compuesto, y no se encontraron registros sanitarios vigentes en Colombia. Los datos de seguridad disponibles son insuficientes para completar una evaluación formal de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin registros aprobados en Colombia |
| Nueva Indicación Predicha | Sin predicciones disponibles |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 — sin datos reales |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué no hay predicciones?

El pipeline TxGNN no devolvió indicaciones candidatas para LANSOPRAZOL en esta ejecución. Se identificaron tres causas probables:

**1. DrugBank ID no disponible.** El campo `drugbank_id` está vacío, lo que puede haber impedido el mapeo correcto del fármaco en el grafo de conocimiento de TxGNN. Sin un identificador válido, el modelo no puede anclar el nodo del fármaco para calcular distancias hacia nodos de enfermedad.

**2. MOA no poblado.** Aunque la consulta a DrugBank devolvió 1 resultado, el mecanismo de acción no fue transferido al Evidence Pack. La conectividad del grafo (vías biológicas compartidas) es uno de los insumos clave para la predicción; su ausencia reduce la cobertura de candidatos.

**3. Posible variante ortográfica.** El INN oficial es *lansoprazole* (grafía anglosajona). Si el modelo fue consultado exclusivamente con la variante española *lansoprazol*, podría existir un problema de mapeo en el índice interno.

> Cabe notar que la consulta a `tfda_package_insert` devolvió 1 resultado exitoso, pero ese contenido no fue integrado en el Evidence Pack. Recuperar ese prospecto podría resolver al menos parcialmente las brechas de seguridad y MOA.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack está incompleto en sus tres dimensiones críticas: ausencia de predicciones TxGNN, cero registros sanitarios en Colombia y brechas bloqueantes en seguridad. No es posible emitir una recomendación de reposicionamiento con la información actual.

**Para avanzar se necesita:**

- Confirmar el DrugBank ID correcto para LANSOPRAZOL y repoblar el campo `drugbank_id` en el Evidence Pack
- Re-ejecutar el pipeline TxGNN con el identificador validado para obtener indicaciones candidatas
- Extraer el mecanismo de acción (MOA) del resultado ya disponible en DrugBank
- Recuperar el prospecto oficial obtenido en la consulta `tfda_package_insert` e integrar advertencias, contraindicaciones e interacciones farmacológicas
- Verificar si existe registro INVIMA vigente en Colombia (el fármaco podría estar registrado bajo un nombre comercial diferente o con grafía alternativa)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

