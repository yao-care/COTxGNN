---
layout: default
title: Denosumab
parent: Solo Predicción del Modelo (L5)
nav_order: 154
evidence_level: L5
indication_count: 2
---

# Denosumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Denosumab: De Indicación Original No Especificada a Retinopatía Diabética No Proliferativa Severa

## Resumen en Una Frase

Denosumab es un anticuerpo que inhibe RANKL y está comercializado en Colombia como XGEVA® y PROLIA®. El registro sanitario consultado no detalla su indicación original.
El modelo TxGNN predice que podría ser efectivo para **retinopatía diabética no proliferativa severa**, pero hoy hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción específica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo repite el nombre "Denosumab") |
| Nueva Indicación Predicha | Retinopatía diabética no proliferativa severa |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Denosumab inhibe RANKL. Los datos detallados de su mecanismo de acción no están disponibles en el paquete de evidencia. Tampoco consta su indicación original, así que no se puede comparar con la nueva indicación.

Un vínculo entre la vía RANKL y las vías vasculares o inflamatorias de la retina en la retinopatía diabética es una **predicción computacional**. Ningún estudio recuperado lo respalda. El puntaje es muy alto (0.996), pero no se puede comprobar por qué el modelo lo asigna. Podría reflejar cercanía en la red del conocimiento con la diabetes y no un mecanismo retiniano real.

Por eso esta predicción debe tratarse como una hipótesis para explorar, no como una recomendación de uso.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Hay 10 registros en total. Los 5 primeros corresponden a solo 2 registros sanitarios únicos, porque XGEVA® aparece repetido.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20052945 | XGEVA® 120 MG/1.7 ML | Solución inyectable | Solo figura el nombre del principio activo (Denosumab), sin texto de indicación |
| 20028103 | PROLIA® | Solución inyectable | Solo figura el nombre del principio activo (Denosumab), sin texto de indicación |

Ambos productos son fabricados por Amgen Manufacturing Limited LLC.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero no cuenta con ensayos clínicos ni literatura directa (L5). Además, faltan datos sobre la indicación original y el mecanismo de acción, por lo que no se puede evaluar su plausibilidad biológica.

Como contexto, la segunda predicción del modelo, retinopatía diabética en general (99.23%), tiene un nivel de evidencia L4 y también queda en Hold:
- El único ensayo de Fase 3 (NCT00925600) evalúa opacidades del cristalino como resultado de seguridad ocular, no la retinopatía.
- Las dos publicaciones tratan sobre desenlaces relacionados con la diabetes en general y aportan solo contexto indirecto.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA para advertencias y contraindicaciones, que hoy bloquea el tamizaje de seguridad.
- Obtener el mecanismo de acción detallado desde DrugBank.
- Confirmar la indicación original aprobada en Colombia.
- Buscar estudios preclínicos o clínicos que relacionen RANKL con la angiogénesis o la inflamación retiniana.
- Revisar la compatibilidad de la vía de administración: el denosumab es inyectable y no hay datos sobre una vía adecuada para la retina.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

