---
layout: default
title: Prilocaine
parent: Solo Predicción del Modelo (L5)
nav_order: 533
evidence_level: L5
indication_count: 10
---

# Prilocaine
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

# Prilocaína: De Lidocaína en Combinaciones (anestesia local) a Conjuntivitis Papilar

## Resumen en Una Frase

La prilocaína es un anestésico local de tipo amida, registrado en Colombia como producto único y en combinación con lidocaína (crema tópica y soluciones inyectables).
El modelo TxGNN predice que podría ser efectiva para **conjuntivitis papilar**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; es solo una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lidocaína combinaciones (anestesia local) |
| Nueva Indicación Predicha | Conjuntivitis papilar |
| Puntaje de Predicción TxGNN | 99.78% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en las fuentes compiladas. Según la información conocida, la prilocaína es un anestésico local de tipo amida que bloquea los canales de sodio dependientes de voltaje, lo que impide la conducción del impulso nervioso. Su eficacia como anestésico local está bien establecida.

La relación con la conjuntivitis papilar, una enfermedad inflamatoria o alérgica de la superficie ocular, es débil. No se identificó un mecanismo plausible que conecte el bloqueo de canales de sodio con el control de la inflamación alérgica ocular, por lo que cualquier vínculo sería especulativo.

Además, la exposición ocular a anestésicos locales conlleva riesgo de toxicidad corneal. La puntuación alta del modelo debe interpretarse como una hipótesis para explorar, no como una señal de eficacia.

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
| 218965 | ANESTECIN® CREMA | Crema tópica | Lidocaína combinaciones | Cancelado |
| 20227791 | PRILOTEKAL® | Solución inyectable | Prilocaína | Cancelado |
| 20023782 | PRESTIGE® PRILOCAÍNA CLORHIDRATO AL 4% | Solución inyectable | Prilocaína | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): hipertensión, epilepsia, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, diabetes mellitus y cetoacidosis diabética, enfermedad coronaria e infarto de miocardio, hemoglobinopatías, paro cardíaco súbito, trastornos de la conducción cardíaca y bloqueo auriculoventricular, insuficiencia respiratoria, glaucoma de ángulo cerrado, miastenia gravis y enfermedades de la unión neuromuscular, deficiencia de butirilcolinesterasa, enfermedad cardiovascular, hipertiroidismo (enfermedad de Graves, tirotoxicosis).
- **Interacciones farmacológicas**: se registraron 22 interacciones, de las cuales se detallan 20 en los datos compilados: 18 de nivel mayor, 1 moderada (morfina liposomal) y 1 menor (hialuronidasa). Las principales de nivel mayor son:
  - Fármacos asociados a metahemoglobinemia: dapsona (sistémica y tópica), primaquina, tafenoquina, cloroquina, quinina, nitrito de amilo, ácido nitroso, óxido nítrico, rasburicasa, sulfasalazina.
  - Otros anestésicos locales: lidocaína (sistémica y tópica), benzocaína tópica, cincocaína tópica.
  - Otros: metoclopramida, nitrato de plata y sulfadiazina de plata tópicos.
- **Riesgo ocular específico**: el uso de anestésicos locales en el ojo puede causar toxicidad corneal, lo que es relevante para las indicaciones oculares predichas.

El texto de advertencias y contraindicaciones del prospecto de INVIMA no está disponible. Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para conjuntivitis papilar se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura. No hay un mecanismo plausible que la sustente y el uso ocular de anestésicos locales implica riesgo de toxicidad corneal. Además, todos los registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción y un análisis mecanístico que justifique un posible efecto en la inflamación alérgica ocular.
- Estudios preclínicos que evalúen eficacia y tolerabilidad ocular (incluida la seguridad corneal).
- Obtener y analizar el prospecto de INVIMA para completar el tamizaje de seguridad.
- Evaluar la viabilidad regulatoria, dado que no hay registros vigentes ni una vía de administración ocular compatible.
- Considerar priorizar otras indicaciones predichas con más respaldo. Por ejemplo, para **neuralgia** (puntaje 99.34%) existen un ensayo de Fase 2 completado con la crema de lidocaína/prilocaína y varias publicaciones clínicas (nivel L2, "Proceed with Guardrails"). Su evidencia se limita a estudios pequeños y antiguos, mayormente con la combinación con lidocaína, y exigiría vigilancia de metahemoglobinemia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

