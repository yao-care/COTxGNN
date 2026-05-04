---
layout: default
title: Avanafil
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 0
---

# Avanafil
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

# Avanafil: Inhibidor de PDE5 — Sin Indicaciones Predichas Disponibles

## Resumen en Una Frase

Avanafil (DB06237) es un inhibidor selectivo de la fosfodiesterasa tipo 5 (PDE5), conocido comercialmente como Stendra® / Spedra®, utilizado para el tratamiento de la disfunción eréctil en adultos. En esta versión del Evidence Pack **no se generaron indicaciones predichas por TxGNN**, por lo que no es posible evaluar formalmente el potencial de reposicionamiento. Adicionalmente, los datos de seguridad y regulatorios presentan brechas significativas que deben resolverse antes de cualquier avance.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Disfunción eréctil (conocimiento farmacológico general; sin registro en Colombia) |
| Nueva Indicación Predicha | No disponible — TxGNN no generó predicciones en esta versión |
| Puntaje de Predicción TxGNN | No disponible |
| Nivel de Evidencia | No evaluable |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué no es Posible Evaluar esta Predicción

El Evidence Pack de Avanafil (v4, fecha de corte: 2026-04-20) presenta dos limitaciones críticas que impiden completar la evaluación estándar de reposicionamiento:

**1. Sin indicaciones predichas.** El array `predicted_indications` está vacío. Esto puede deberse a que el modelo TxGNN aún no procesó este candidato, a que el candidato no alcanzó el umbral mínimo de puntuación para generar predicciones, o a un fallo en la etapa de mapeo de enfermedades. Sin este insumo central, no es posible aplicar el formato estándar del informe ni construir el análisis de reposicionamiento.

**2. Brechas de datos bloqueantes.** Dos brechas críticas (DG001 y DG002) impiden la evaluación de seguridad inicial (S1):
- **DG001 (Severidad: Bloqueante):** Las advertencias y contraindicaciones del prospecto oficial no fueron extraídas, bloqueando por completo el análisis de seguridad.
- **DG002 (Severidad: Alta):** El mecanismo de acción (MOA) no está disponible desde DrugBank, lo que impide el análisis de relevancia mecanística.

Desde el conocimiento farmacológico general, Avanafil es un inhibidor selectivo de PDE5 con mayor selectividad por PDE5 frente a PDE6 comparado con sildenafil, lo que se asocia a un perfil de efectos visuales más favorable. Sin embargo, estos datos no forman parte del Evidence Pack entregado y no pueden utilizarse como base formal para un análisis de reposicionamiento.

---

## Información de Mercado en Colombia

Avanafil **no cuenta con registros sanitarios activos en Colombia (INVIMA)** a la fecha de corte del presente reporte. No se registran licencias, formas farmacéuticas aprobadas ni indicaciones locales.

---

## Consideraciones de Seguridad

Consultar el prospecto del fabricante para información sobre advertencias, contraindicaciones e interacciones farmacológicas. Los datos de seguridad no pudieron ser extraídos automáticamente en esta versión del Evidence Pack (ver brechas DG001).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack está incompleto en sus insumos mínimos requeridos: no hay indicaciones predichas por TxGNN, el MOA no está disponible, los datos de seguridad son inaccesibles, y el fármaco no tiene presencia regulatoria en Colombia. No es posible emitir una recomendación de reposicionamiento sin estos elementos.

**Para avanzar se necesita:**
- Completar el procesamiento TxGNN para este candidato y poblar el campo `predicted_indications`
- Obtener el MOA desde la API de DrugBank (remediación DG002)
- Descargar y analizar el prospecto oficial para extraer advertencias y contraindicaciones (remediación DG001)
- Evaluar la viabilidad de un registro sanitario en Colombia como paso previo a cualquier estrategia de entrada al mercado
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

