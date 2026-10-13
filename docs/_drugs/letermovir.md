---
layout: default
title: Letermovir
parent: Solo Predicción del Modelo (L5)
nav_order: 390
evidence_level: L5
indication_count: 1
---

# Letermovir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Letermovir: De Letermovir (CMV) a Candidiasis Vulvovaginal

## Resumen en Una Frase

Letermovir es un antiviral específico contra el citomegalovirus (CMV), registrado en Colombia bajo el nombre PREVYMIS en tabletas.
El modelo TxGNN predice que podría ser efectivo para **candidiasis vulvovaginal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LETERMOVIR (el registro sanitario no detalla el texto de la indicación) |
| Nueva Indicación Predicha | Candidiasis vulvovaginal |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según el conocimiento farmacológico general, letermovir es un antiviral específico contra el CMV que inhibe el complejo terminasa viral (subunidades pUL56/pUL51/pUL89), bloqueando el corte y empaquetamiento del ADN viral.

La candidiasis vulvovaginal es una infección fúngica. Los hongos del género *Candida* no tienen un blanco equivalente al complejo terminasa del CMV, por lo que no se esperaría actividad antifúngica. **No se identifica un vínculo mecanístico creíble** entre la indicación original y la nueva.

El puntaje alto de TxGNN (0.9988) es una predicción del grafo de conocimiento. Puede reflejar la cercanía en la red con otros fármacos antiinfecciosos o características compartidas del grafo, y no necesariamente plausibilidad biológica. Cualquier hipótesis requeriría validación experimental independiente, por ejemplo pruebas de susceptibilidad in vitro frente a *Candida* spp.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20194849 (cancelado) | PREVYMIS 240MG TABLETAS | Tableta | LETERMOVIR |

El fabricante es Merck Sharp & Dohme LLC. La única vía de administración registrada es la oral. Dado que el único registro está cancelado, actualmente no hay presentación vigente en el mercado colombiano.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. En la muestra analizada predominan las de nivel moderado y destacan tres de nivel **mayor**:
  - Eliglustat
  - Naloxegol
  - Cisaprida

  Otras interacciones de nivel moderado incluyen corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), antidiabéticos (pioglitazona, saxagliptina, glimepirida, clorpropamida, acetohexamida), inhibidores de bomba de protones (omeprazol, lansoprazol), aprepitant, claritromicina, naldemedina y nitisinona.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y sin un vínculo mecanístico plausible, ya que letermovir actúa sobre un blanco viral sin equivalente en *Candida*. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Pruebas de susceptibilidad in vitro de *Candida* spp. frente a letermovir como validación mínima
- Datos del mecanismo de acción desde DrugBank para analizar posibles vínculos mecanísticos
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones) antes de cualquier evaluación de seguridad
- Evaluar la compatibilidad de vía de administración (la presentación registrada es solo oral)
- Aclarar la situación regulatoria del producto en Colombia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

