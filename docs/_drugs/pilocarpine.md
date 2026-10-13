---
layout: default
title: Pilocarpine
parent: Solo Predicción del Modelo (L5)
nav_order: 515
evidence_level: L5
indication_count: 1
---

# Pilocarpine
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

# Pilocarpina: De Indicación No Especificada a Glaucoma Hereditario Primario

## Resumen en Una Frase

Pilocarpina es un agonista colinérgico muscarínico que contó con registros sanitarios en Colombia (solución oftálmica y tabletas), actualmente todos cancelados; el texto de indicación registrado solo menciona el nombre del fármaco.
El modelo TxGNN predice que podría ser efectivo para **glaucoma hereditario primario**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "Pilocarpina") |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 (0 vigentes, 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este reporte no incluyen el mecanismo de acción registrado del fármaco. Según la farmacología general, la pilocarpina es un agonista colinérgico muscarínico con preferencia por el receptor M3. En el ojo contrae el músculo ciliar y el esfínter del iris, lo que abre la malla trabecular, aumenta la salida convencional del humor acuoso y reduce la presión intraocular (PIO). Es un fundamento farmacológico plausible y bien establecido para el glaucoma en general, en especial las formas de ángulo cerrado y ángulo abierto.

Sin embargo, la relación con la indicación predicha es limitada. En el glaucoma hereditario primario (congénito o juvenil), la patología principal es un desarrollo anómalo de la malla trabecular o del ángulo (disgenesia). En ese contexto los mióticos podrían ser menos eficaces, y la cirugía suele ser el tratamiento de primera línea.

El puntaje de TxGNN (0.998) es solo una predicción del modelo. No hay ensayos ni literatura aportados que respalden el uso específico en esta forma de glaucoma.

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
| 39261 | ISOPTO CARPINA® 2% | Solución oftálmica | PILOCARPINA | Cancelado |
| 20097979 | PICARPIN® | Tableta recubierta | PILOCARPINA | Cancelado |
| 20091048 | CARPIX® TABLETA RECUBIERTA | Tableta cubierta con película | PILOCARPINA | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no provienen del prospecto)**:
  - Oculares: glaucoma de ángulo cerrado, queratitis, queratoconjuntivitis, iritis, uveítis, iridociclitis, desprendimiento de retina.
  - Respiratorias: asma, enfermedad pulmonar obstructiva crónica (EPOC, incluida la de inicio temprano severo), enfermedad bronquial.
  - Hepatobiliares: insuficiencia hepática, colelitiasis, colecistolitiasis, coledocolitiasis, colecistitis, enfermedad de las vías biliares, ictericia obstructiva.
  - Renales: nefrolitiasis (incluida la susceptibilidad por SLC26A1), nefropatía aguda por uratos.
- **Interacciones Farmacológicas**: se identificaron 102 interacciones en total. Las de nivel moderado más relevantes son con fármacos antimuscarínicos/anticolinérgicos (efecto farmacológico opuesto): hiosciamina, atropina (incluida oftálmica), glicopirronio (incluido tópico), clidinio, diciclomina, mepenzolato, metescopolamina, propantelina, escopolamina (incluida oftálmica) y trospio. Otras interacciones, de nivel no clasificado, incluyen pantoprazol, clotrimazol, morfina, metformina, omeprazol, lansoprazol y epinefrina.

Nota: la información de advertencias y contraindicaciones del prospecto no está disponible; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos ni literatura, y la fisiopatología del glaucoma hereditario primario (disgenesia del ángulo) hace dudosa la eficacia de un miótico. Además, todos los registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Revisión de literatura específica sobre el uso de pilocarpina en glaucoma congénito o juvenil.
- Obtener el prospecto de INVIMA para evaluar advertencias y contraindicaciones.
- Confirmar el mecanismo de acción en DrugBank.
- Definir la vía de administración requerida (tópica oftálmica) y su disponibilidad, dado que no hay registros vigentes.
- Evaluar si la indicación aporta valor frente al tratamiento quirúrgico de primera línea.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

