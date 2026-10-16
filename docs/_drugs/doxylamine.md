---
layout: default
title: Doxylamine
parent: Solo Predicción del Modelo (L5)
nav_order: 236
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Doxylamine: nueva indicación predicha, Urticaria alérgica (nivel de evidencia L5). Indicación original: Doxilamina. Combinaciones"
---

# Doxylamine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Doxilamina: De Combinaciones de Doxilamina a Urticaria Alérgica

## Resumen en Una Frase

Doxilamina es un antihistamínico H1 de primera generación (clase etanolamina), registrado en Colombia bajo la indicación genérica "Doxilamina. Combinaciones".
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**, con un puntaje muy alto (99.85%).
Sin embargo, actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: la evidencia se limita a la predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Doxilamina. Combinaciones |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L5 (solo predicción del modelo, sin estudios reales; el análisis mecanístico de clase sugiere un componente L4 en el sentido de plausibilidad farmacológica, pero sin estudios específicos) |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción específico de este fármaco en los datos compilados. Según la información conocida de la clase, la doxilamina es un antihistamínico H1 de primera generación (etanolamina) con propiedades anticolinérgicas y sedantes. Su eficacia como antihistamínico está establecida a nivel de clase, y mecanísticamente podría ser aplicable a la urticaria alérgica.

La urticaria alérgica está mediada por histamina liberada por mastocitos, que produce ronchas y eritema. El bloqueo del receptor H1 es, por tanto, un mecanismo directamente relevante, y los antihistamínicos H1 de primera generación se han utilizado históricamente para esta condición como clase.

Es importante matizar: este vínculo se apoya en la farmacología de clase y no en datos específicos de doxilamina. Además, las guías actuales prefieren antihistamínicos de segunda generación no sedantes, lo que limita el valor agregado de doxilamina en esta indicación.

### Otras indicaciones predichas (para contexto)

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Recomendación | Comentario |
|------|------|------|------|------|
| Enfermedad de la cavidad nasal | 99.36% | L5 | Hold | Categoría amplia e inespecífica; el efecto antihistamínico y de sequedad anticolinérgica podría reducir rinorrea y congestión, pero no puede vincularse a una patología definida |
| Laringofaringitis aguda | 99.34% | L5 | Hold | Generalmente infecciosa; el beneficio sería solo sintomático (goteo posnasal, tos) |
| Urticaria por frío | 99.26% | L5 | Research Question | Urticaria física mediada por histamina; plausible a nivel de clase, pero sin evidencia específica y con preferencia guiada por antihistamínicos de segunda generación |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20069694 | PLURIAMIN® Tabletas de Liberación Retardada (Laboratorio Franco Colombiano - Lafrancol S.A.S.) | Tableta de liberación retardada | Doxilamina. Combinaciones | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento asocia a la doxilamina con contraindicaciones en las siguientes condiciones, lo que es coherente con su perfil anticolinérgico y sedante de clase:
  - **Oculares:** glaucoma de ángulo cerrado, hipertensión ocular.
  - **Urinarias:** hiperplasia prostática benigna, obstrucción del cuello vesical.
  - **Cardiovasculares:** hipertensión, enfermedad coronaria, infarto de miocardio, aterosclerosis, taquicardia ventricular.
  - **Hepáticas y digestivas:** insuficiencia hepática, hepatopatía, pancreatitis, enfermedad de la vesícula biliar, úlcera péptica.
  - **Endocrinas y metabólicas:** diabetes mellitus, cetoacidosis diabética, hipertiroidismo (enfermedad de Graves, tirotoxicosis).
  - **Otras:** hemoglobinopatía, intoxicación por paracetamol, abuso/dependencia de sustancias.
- **Interacciones farmacológicas:** se identificaron 100 interacciones en total. Las de mayor gravedad son de nivel **Mayor**, con **cloruro de potasio** y **citrato de potasio**. Entre las de nivel **Moderado** destacan:
  - Otros anticolinérgicos: atropina, escopolamina, hiosciamina, glicopirronio, diciclomina, clidinio, propantelina, mepenzolato, metescopolamina.
  - Depresores del SNC y opioides: morfina (incluida liposomal), opio, loperamida, eluxadolina.
  - Cannabinoides: dronabinol, nabilona.
  - Otros: metoclopramida.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para información de seguridad adicional.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a una predicción computacional (puntaje 99.85%) sin ensayos clínicos ni literatura. Además, el único registro sanitario en Colombia está cancelado, y las guías actuales prefieren antihistamínicos de segunda generación no sedantes para la urticaria, lo que reduce el valor agregado del reposicionamiento.

**Para avanzar se necesita:**
- Datos del mecanismo de acción específico del fármaco (DrugBank).
- Advertencias y contraindicaciones del prospecto de INVIMA, necesarias para el tamizaje de seguridad.
- Búsqueda de ensayos clínicos y literatura específicos de doxilamina en urticaria.
- Análisis comparativo frente a antihistamínicos de segunda generación (eficacia, sedación, perfil anticolinérgico).
- Verificación de la situación regulatoria: confirmar si existe algún producto vigente con doxilamina en Colombia y la compatibilidad de las vías de administración.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

