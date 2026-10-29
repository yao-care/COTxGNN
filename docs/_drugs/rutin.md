---
layout: default
title: Rutin
parent: Solo Predicción del Modelo (L5)
nav_order: 574
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-29
description: "Rutin: nueva indicación predicha, Enfermedad fibroquística de la mama (nivel de evidencia L5). Indicación original: Multivitaminas y otros minerales, incluidas combinaciones"
monitor_inn: "rutin"
predicted_indications: ["breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia", "vulvovaginal candidiasis", "breast abscess", "fat necrosis of breast", "vaginitis (disease)"]
---

# Rutin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Rutina: De Multivitamínicos a Enfermedad Fibroquística de la Mama
{: .text-alpha }

## Resumen en Una Frase

La rutina es un flavonoide que en Colombia se registró como componente de productos multivitamínicos (SUPRAVITAL), con y sin hierro.
El modelo TxGNN predice que podría ser efectiva para **enfermedad fibroquística de la mama**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Multivitaminas y otros minerales, incluidas combinaciones |
| Nueva Indicación Predicha | Enfermedad fibroquística de la mama |
| Puntaje de Predicción TxGNN | 0.9974 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Autorizado pero no comercializado (registros: None) |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la rutina es un flavonoide con propiedades antioxidantes, antiinflamatorias y de protección capilar/venosa. Su uso registrado en Colombia fue como componente de multivitamínicos, no como tratamiento de una enfermedad específica.

La relación entre la indicación original (suplementación nutricional) y la nueva (cambios benignos del tejido mamario) es débil. Teóricamente, las propiedades antioxidantes y antiinflamatorias podrían relacionarse con cambios benignos de la mama, pero este vínculo no está verificado con los datos compilados.

Cabe señalar que varias de las predicciones siguientes del modelo (adenosis apocrina de la mama, adenosis de conductos romos, displasia mamaria benigna) son variantes o sinónimos cercanos de la enfermedad fibroquística, por lo que probablemente no constituyen señales independientes. Otras predicciones incluyen candidiasis vulvovaginal, absceso mamario, necrosis grasa de la mama y vaginitis, todas con puntajes de 0.9909 a 0.9922 y también sin respaldo clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (enfermedad fibroquística de la mama).

Para la predicción de vaginitis (una indicación secundaria) se recuperaron dos publicaciones, pero no son relevantes: tratan sobre extractos de plantas en modelos de ovario poliquístico en ratas y no estudian la rutina ni la vaginitis.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19908281 | SUPRAVITAL | Cápsula blanda | Multivitaminas y otros minerales, incluidas combinaciones (vigente) |
| 19942493 | SUPRAVITAL PLUS | Cápsula blanda | Multivitaminas más hierro (vigente) |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto de prospecto): anemia de células falciformes, persistencia hereditaria de hemoglobina fetal, hiperoxaluria primaria, hemocromatosis hereditaria, hemosiderosis, enfermedad del metabolismo del hierro y enfermedad de Wilson. Es probable que parte de estas señales se deba a los productos combinados con hierro.

No se encontraron interacciones farmacológicas registradas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las indicaciones predichas están en nivel L5: son solo predicciones del modelo, sin ensayos clínicos ni literatura que las respalden. Además, el producto no tiene registros vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar el análisis de advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad)
- Consultar el mecanismo de acción en DrugBank
- Realizar una búsqueda dirigida de literatura sobre rutina y enfermedad fibroquística de la mama (estudios preclínicos y clínicos)
- Evaluar la compatibilidad de vía de administración y formulación, dado que no hay registros vigentes
- Decidir si se justifica un estudio preclínico o un piloto antes de reconsiderar la decisión
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

