---
layout: default
title: Fluorometholone
parent: Solo Predicción del Modelo (L5)
nav_order: 296
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluorometholone: nueva indicación predicha, Vasculitis postinfecciosa (nivel de evidencia L5). Indicación original: Fluorometolona"
monitor_inn: "fluorometholone"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome", "punctate epithelial keratoconjunctivitis", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Fluorometholone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Fluorometolona: De Inflamación Ocular (Fluorometolona) a Vasculitis Postinfecciosa

## Resumen en Una Frase

La fluorometolona es un corticosteroide oftálmico tópico, aprobado en Colombia (registros hoy cancelados) para la inflamación ocular.
El modelo TxGNN predice que podría ser efectivo para **vasculitis postinfecciosa**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fluorometolona (corticosteroide oftálmico; el registro no detalla una indicación clínica más específica) |
| Nueva Indicación Predicha | Vasculitis postinfecciosa |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, la fluorometolona es un corticosteroide sintético que actúa sobre el receptor de glucocorticoides (NR3C1) y se usa para tratar la conjuntivitis inflamatoria y la inflamación de la superficie ocular que responde a esteroides.

Los corticosteroides se emplean en vasculitis de origen inmunomediado, por lo que existe un vínculo teórico entre su acción antiinflamatoria e inmunosupresora y la indicación predicha. Sin embargo, la fluorometolona se presenta como suspensión oftálmica tópica, con exposición sistémica mínima. Esto limita mucho su plausibilidad para una enfermedad vascular sistémica.

En resumen, el vínculo mecanístico es teórico y no está respaldado por estudios. Otras predicciones del modelo (por ejemplo, queratoconjuntivitis epitelial punteada, iridociclitis inducida por cristalino o crisis glaucomatociclítica) son más coherentes con la vía de administración ocular, aunque tampoco cuentan con evidencia directa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Todos los registros sanitarios están cancelados; actualmente no hay productos vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19959732 | FLUOFTAL® 0.1 % Suspensión Oftálmica | Suspensión oftálmica | Fluorometolona (cancelado) |
| 20050754 | FLU-SURE T® Suspensión Oftálmica | Suspensión oftálmica | Tetrizolina, combinaciones (cancelado) |
| 20058411 | FLUOMAX® Suspensión Oftálmica | Suspensión oftálmica | Fluorometolona (cancelado) |

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones del prospecto. Como referencia adicional, el grafo de conocimiento utilizado por el modelo (no el texto del prospecto) asocia al fármaco con las siguientes contraindicaciones:

- **Contraindicaciones según el grafo de conocimiento**:
  - Oculares/infecciosas: queratitis por virus del herpes simple, infección ocular infecciosa, conjuntivitis, infección fúngica del ojo, infección viral del ojo, tuberculosis ocular.
  - Presión intraocular: glaucoma de ángulo abierto, hipertensión ocular.
  - Otras: pigmentación corneal, porfiria (hereditaria y del metabolismo de porfirinas), diabetes mellitus, cetoacidosis diabética, deficiencia de G6PD, enfermedad por almacenamiento de glucógeno, cistinuria, galactosemia.
- **Interacciones Farmacológicas**: Se identificaron 11 posibles interacciones (fuente DDInter), todas con nivel de gravedad no clasificado: doxiciclina, salbutamol, ciclosporina, paracetamol, digoxina, brimonidina, cefalexina, ácido alendrónico, aciclovir, diazepam y fenofibrato. Además, el fármaco actúa sobre el receptor de glucocorticoides (NR3C1).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto del modelo, pero no cuenta con ensayos clínicos ni literatura (nivel L5). Además, la vía oftálmica tópica con exposición sistémica mínima y la ausencia de registros vigentes en Colombia reducen su viabilidad para una vasculitis sistémica.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar advertencias y contraindicaciones.
- Confirmar el mecanismo de acción en DrugBank.
- Realizar una revisión de literatura específica sobre corticosteroides en vasculitis postinfecciosa.
- Evaluar la compatibilidad de vía de administración y formulación (la vía actual es solo oftálmica).
- Considerar priorizar indicaciones oculares predichas (queratoconjuntivitis epitelial punteada, iridociclitis inducida por cristalino, crisis glaucomatociclítica), más coherentes con la vía de administración, con vigilancia de la presión intraocular.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

