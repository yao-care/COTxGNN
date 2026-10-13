---
layout: default
title: Phenol
parent: Solo Predicción del Modelo (L5)
nav_order: 512
evidence_level: L5
indication_count: 8
---

# Phenol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Fenol: De Combinaciones/Fenol a Acrodermatitis Crónica Atrófica

## Resumen en Una Frase

El fenol es un compuesto antiséptico y cáustico, registrado en Colombia en soluciones bucales, bucofaríngeas y óticas (indicación registrada: "FENOL" y "COMBINACIONES").
El modelo TxGNN predice que podría ser efectivo para **acrodermatitis crónica atrófica**, con un puntaje muy alto (99,95 %), pero sin **ningún ensayo clínico** ni **publicación** que respalde esta predicción.
Se trata de una predicción puramente computacional, sin sustento mecanístico identificado.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | FENOL (registro sanitario sin indicación terapéutica detallada) |
| Nueva Indicación Predicha | Acrodermatitis crónica atrófica |
| Puntaje de Predicción TxGNN | 99,95 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Por conocimiento general, el fenol actúa desnaturalizando proteínas, con efecto antiséptico, cáustico y neurolítico; se usa en soluciones de aplicación local en boca, garganta y oído, y en peelings químicos.

La acrodermatitis crónica atrófica es la fase cutánea tardía de la borreliosis de Lyme y se trata con antibióticos. No se identificó un vínculo mecanístico plausible entre las acciones del fenol y esta enfermedad.

El alto puntaje (rank 1459 en el modelo) refleja proximidad en el grafo de conocimiento, no un mecanismo demostrado. Por ello, esta predicción debe considerarse una hipótesis sin respaldo farmacológico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para acrodermatitis crónica atrófica.

> Nota: entre las demás predicciones, solo "queloide acneico" (acné queloide) tiene un estudio sobre fenol: un peeling de fenol modificado (Exoderm) para arrugas y cicatrices de acné (PMID 17204096, 2007, *The Journal of Dermatology*). Este estudio no corresponde a la indicación principal de este informe.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20229729 | NOXPIRIN® SOLUCIÓN BUCAL | Solución bucal | FENOL | Cancelado |
| 20113559 | BUCALIV SPRAY® | Solución bucofaríngea | FENOL | Cancelado |
| 20049882 | OTIFIX® SOLUCIÓN ÓTICA | Solución ótica | COMBINACIONES | Cancelado |

---

## Consideraciones de Seguridad

- **Posibles contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto de prospecto): epilepsia, enfermedad hepática, enfermedad de la vesícula biliar, diabetes mellitus, cetoacidosis diabética, neutropenia, agranulocitosis, paro cardíaco súbito, enfermedad de la conducción cardíaca, bloqueo auriculoventricular, dermatitis, insuficiencia respiratoria, enfermedad vascular periférica, claudicación intermitente, apendicitis, úlcera péptica activa, infecciones por herpes simple, herpes zóster y citomegalovirus, verrugas comunes y virus del papiloma humano anogenital, leucoencefalopatía multifocal progresiva, cáncer y linfomas.
- **Consideraciones adicionales señaladas en el análisis:** el fenol es tóxico a nivel sistémico y puede absorberse por vía dérmica, lo que preocupa especialmente en neonatos; además, es irritante y corrosivo para tejidos oculares.
- No se encontraron interacciones farmacológicas registradas.

Consultar el prospecto para la información de seguridad oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible; además, el fenol tiene un perfil de toxicidad desfavorable y todos sus registros en Colombia están cancelados.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consultar DrugBank).
- Prospecto de INVIMA con advertencias y contraindicaciones oficiales.
- Una justificación biológica que relacione el fenol con la borreliosis de Lyme cutánea tardía, o priorizar otras predicciones con algún respaldo, como el uso en cicatrices (acné queloide), que sigue siendo solo una pregunta de investigación (L4) y exige cautela por el riesgo de empeorar cicatrices queloides.
- Evaluación de compatibilidad de vía de administración y de formulación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

