---
layout: default
title: Caplacizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Caplacizumab
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

# Caplacizumab: De Púrpura Trombótica Trombocitopénica Adquirida a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Caplacizumab es un nanocuerpo anti-factor de von Willebrand (vWF) que se usa en la púrpura trombótica trombocitopénica adquirida (PTT). El registro sanitario colombiano solo repite el nombre del fármaco y no describe la indicación.
El modelo TxGNN predice que podría ser efectivo para el **trastorno primario de liberación plaquetaria**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Además, el mecanismo del fármaco sugiere un posible aumento del riesgo de sangrado.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto solo dice «CAPLACIZUMAB»); en la práctica clínica, PTT adquirida |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99.9998% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos de mecanismo de acción en DrugBank. Según la información disponible, caplacizumab bloquea el dominio A1 del vWF e impide su unión al receptor plaquetario GPIb. Así evita la adhesión plaquetaria y la formación de microtrombos, que es la base de su uso en la PTT adquirida.

La relación entre la indicación original y la nueva es débil. La PTT es una enfermedad trombótica, con exceso de adhesión plaquetaria. Un trastorno de liberación plaquetaria es un problema hemorrágico, con función plaquetaria deficiente. El puntaje alto del grafo parece reflejar cercanía en la ontología (plaquetas, vWF) y no una razón terapéutica.

Mecanísticamente, el efecto esperado es contrario al deseado. Reducir aún más la adhesión plaquetaria podría aumentar el sangrado en un paciente que ya tiene un defecto plaquetario. Por eso esta predicción se considera solo una señal del modelo, sin respaldo mecanístico ni clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20176684 | CABLIVI® (SANOFI-AVENTIS DE COLOMBIA S.A.) | Polvo liofilizado para reconstituir a solución inyectable | CAPLACIZUMAB (el registro no detalla la indicación) |

Los cinco registros extraídos corresponden al mismo número sanitario y son idénticos, por lo que se muestran en una sola fila. El total reportado es de 8 registros.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Por su mecanismo, el fármaco inhibe la adhesión plaquetaria mediada por vWF y se espera un mayor riesgo de sangrado. Este riesgo es especialmente relevante en pacientes con trastornos hemorrágicos plaquetarios. No se encontraron interacciones farmacológicas registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura. El mecanismo de caplacizumab podría empeorar el sangrado en un trastorno plaquetario, por lo que no hay base para avanzar.

**Para avanzar se necesita:**
- Evidencia preclínica que muestre un beneficio plausible, algo que hoy no existe.
- Evaluación de seguridad hemorrágica específica para pacientes con defectos plaquetarios.
- Obtener del prospecto de INVIMA las advertencias y contraindicaciones.
- Obtener el mecanismo de acción desde DrugBank.
- Aclarar la indicación aprobada en el registro colombiano, que hoy solo indica el nombre del fármaco.

**Nota:** en esta misma corrida, la predicción para la **púrpura trombótica trombocitopénica** (posición 5) tiene evidencia L1. Incluye un ECA de Fase 2 (TITAN), un ECA de Fase 3 (HERCULES) y un estudio de Fase 3 de un solo brazo. Sin embargo, es una indicación ya establecida y avalada por guías, no un reposicionamiento nuevo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

