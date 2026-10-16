---
layout: default
title: Cefpodoxime
parent: Solo Predicción del Modelo (L5)
nav_order: 143
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Cefpodoxime: nueva indicación predicha, Susceptibilidad a la osteoartritis (osteoarthritis susceptibility) (nivel de evidencia L5). Indicación original: CEFPODOXIMA"
---

# Cefpodoxime
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Cefpodoxima: De CEFPODOXIMA a Osteoartritis (susceptibilidad)

## Resumen en Una Frase

Cefpodoxima es un antibiótico cefalosporínico de tercera generación, registrado en Colombia bajo la indicación "CEFPODOXIMA" (el texto de indicación no detalla las infecciones específicas).
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad a la osteoartritis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; es solo una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CEFPODOXIMA (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Susceptibilidad a la osteoartritis (osteoarthritis susceptibility) |
| Puntaje de Predicción TxGNN | 99.35% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según el conocimiento general, la cefpodoxima es una cefalosporina de tercera generación que inhibe la síntesis de la pared celular bacteriana al unirse a las proteínas fijadoras de penicilina. Su eficacia se asocia a infecciones bacterianas, no a enfermedades articulares.

**Con los datos compilados, no se identifica un vínculo mecanístico plausible** entre un betalactámico antibacteriano y la susceptibilidad genética a la osteoartritis. Además, "susceptibilidad" es un concepto de riesgo genético y no una condición clínica tratable, lo que debilita aún más la utilidad práctica de esta predicción.

El puntaje alto de TxGNN (99.35%) proviene de un grafo de conocimiento y no está respaldado por estudios reales. Las otras predicciones del modelo tampoco cuentan con respaldo: osteoartritis (99.25%) y artritis reumatoide (99.24%), ambas con 0 ensayos y 0 publicaciones, y sin acción antiinflamatoria, condroprotectora, analgésica ni inmunomoduladora conocida de la cefpodoxima que las justifique.

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
| 19992617 | DOXCEF® SUSPENSION (Laboratorios Legrand S.A.) – cancelado | Polvo para reconstituir a suspensión oral | CEFPODOXIMA |
| 20248427 | CEFPODOXIME PROXETIL 200 MG TABLETAS RECUBIERTAS (Hetero Labs Limited) – cancelado | Tableta recubierta | CEFPODOXIMA |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 78 interacciones en total; las 20 listadas en los datos compilados son de nivel moderado. Los grupos principales son:
  - **Antiácidos y sales de aluminio, calcio y magnesio**: hidróxido de aluminio, carbonato de calcio, magaldrato, carbonato, hidróxido y óxido de magnesio.
  - **Antagonistas H2**: famotidina, ranitidina (incluida ranitidina con citrato de bismuto), cimetidina, nizatidina.
  - **Inhibidores de la bomba de protones**: omeprazol, esomeprazol, lansoprazol, dexlansoprazol, rabeprazol, pantoprazol.
  - **Otros**: balsalazida y los aminoglucósidos kanamicina y neomicina.

  Los fármacos que reducen la acidez gástrica suelen disminuir la absorción de la cefpodoxima proxetilo.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5), sin ensayos clínicos ni publicaciones, y no existe un vínculo mecanístico plausible entre una cefalosporina antibacteriana y la susceptibilidad a la osteoartritis. Además, los dos registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), actualmente pendiente y de carácter bloqueante para la evaluación de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Demostrar una hipótesis biológica plausible que conecte el fármaco con la patología articular.
- Considerar priorizar "osteoartritis" como indicación clínica en lugar de "susceptibilidad", y realizar estudios preclínicos antes de cualquier ensayo.
- Aclarar la situación regulatoria en Colombia, dado que no hay registros vigentes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

