---
layout: default
title: Adapalene
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 1
---

# Adapalene
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

Usando el skill `txgnn-pipeline` como referencia de contexto. Ahora procedo a generar el informe de evaluación de reposicionamiento basado en el Evidence Pack proporcionado.

---

# Adapalene: De Acné Vulgaris a Zinc Elevado en Plasma

## Resumen en Una Frase

Adapalene es un retinoide sintético de tercera generación, ampliamente utilizado en dermatología para el tratamiento tópico del acné vulgaris.
El modelo TxGNN predice que podría ser efectivo para **Zinc Elevado en Plasma** (*zinc, elevated plasma*),
sin embargo, actualmente **no existe ningún ensayo clínico ni publicación científica** que respalde esta dirección — la predicción se sustenta exclusivamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Sin registros sanitarios en Colombia (conocido por acné vulgaris) |
| Nueva Indicación Predicha | Zinc Elevado en Plasma |
| Puntaje de Predicción TxGNN | 99.51% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | No Comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, adapalene es un retinoide naphthaleno-ácido que actúa selectivamente sobre los receptores nucleares RAR-β y RAR-γ del ácido retinoico. A diferencia de los retinoides de primera generación, no se une a las proteínas transportadoras de retinoides en plasma (CRABP), lo que le confiere un perfil de tolerabilidad tópica más favorable. Su eficacia en acné vulgaris ha sido ampliamente demostrada en ensayos de Fase 3.

Existe una conexión biológica plausible entre los retinoides y la homeostasis del zinc: la vitamina A y sus análogos requieren dedos de zinc (*zinc fingers*) en los receptores RAR/RXR para su activación transcripcional. El zinc es cofactor esencial en la cadena de señalización retinoides → RAREs (elementos de respuesta al ácido retinoico). Teóricamente, la modulación de estas vías por adapalene podría influir en el equilibrio de zinc intracelular y plasmático, activando o reprimiendo genes involucrados en el transporte y metabolismo del zinc (ej. metalotioneínas, transportadores ZIP/ZnT).

Sin embargo, esta conexión es especulativa: la predicción de TxGNN con puntaje de 99.51% señala una asociación estadística en el grafo de conocimiento biomédico, pero no ha sido validada experimentalmente. La indicación "zinc, elevated plasma" es una entidad metabólica poco convencional como objetivo terapéutico primario, lo que refuerza la necesidad de investigación traslacional antes de avanzar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje TxGNN es muy alto (99.51%), la ausencia total de evidencia clínica y preclínica publicada (nivel L5), combinada con el hecho de que "zinc elevado en plasma" es una indicación atípica para un retinoide tópico, no justifica avanzar hacia desarrollo clínico en este momento. Además, adapalene no está comercializado en Colombia, lo que representa una barrera regulatoria adicional.

**Para avanzar se necesita:**
- Obtener datos del mecanismo de acción (MOA) desde DrugBank/FDA label para confirmar la plausibilidad del vínculo con el metabolismo del zinc
- Realizar búsqueda bibliográfica ampliada: retinoides + zinc homeostasis + plasma zinc levels
- Estudios preclínicos in vitro que midan niveles de zinc intracelular y plasmático bajo exposición a adapalene
- Evaluar la relevancia clínica de "zinc elevado en plasma" como entidad nosológica tratable (diagnóstico diferencial: hiperzincemia primaria vs. secundaria)
- Configurar alerta de monitoreo en ClinicalTrials.gov y PubMed para evidencia emergente sobre esta combinación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

