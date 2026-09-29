---
layout: default
title: Metformin
parent: Solo Predicción del Modelo (L5)
nav_order: 278
evidence_level: L5
indication_count: 5
---

# Metformin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Metformina: De Indicación No Especificada en el Registro a Síndrome de la Persona Rígida Clásico

## Resumen en Una Frase

La metformina está comercializada en Colombia, pero el texto de indicación del registro sanitario solo dice «Metformina» y no detalla el uso aprobado.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de la persona rígida clásico**, con un puntaje alto (99.45%).
Hasta ahora hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, así que se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro INVIMA solo indica «Metformina») |
| Nueva Indicación Predicha | Síndrome de la persona rígida clásico (*classic stiff person syndrome*) |
| Puntaje de Predicción TxGNN | 99.45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Tampoco hay una indicación original documentada que permita compararla con la nueva. Por eso no se puede establecer una relación sólida entre ambas.

Como hipótesis, la metformina activa la vía AMPK y modula mTOR, lo que podría tener un efecto inmunomodulador. El síndrome de la persona rígida es un trastorno autoinmune, a menudo asociado a anticuerpos anti-GAD65. Este vínculo es especulativo y no está validado. Se apoya únicamente en el puntaje del modelo.

Otras predicciones del modelo para este fármaco tienen el mismo nivel de evidencia (L5, sin ensayos ni literatura):

| Enfermedad predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Síndrome de la extremidad rígida focal | 99.45% | Mismo puntaje que el síndrome clásico, probablemente por la misma señal del modelo; no es evidencia independiente |
| Opsismodisplasia | 99.40% | Posible vínculo por la vía PI3K/Akt e insulina (gen INPPL1/SHIP2); hipótesis sin verificar |
| Síndrome de disfunción sensible a tiamina | 99.40% | Posible interacción con transportadores de tiamina; podría ser un riesgo de seguridad más que un beneficio |
| Lipodistrofia localizada inducida por fármacos | 99.06% | Vínculo indirecto y especulativo por la sensibilidad a la insulina en el tejido adiposo |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Los datos recibidos contienen 5 filas idénticas del mismo registro sanitario. Se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20235551 | WILMETINA 500 MG TABLETAS RECUBIERTAS (BRAINPHARMA S.A.S.) | Tableta recubierta (vía oral) | Metformina (sin detalle de indicación) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5): no hay ensayos clínicos, literatura ni mecanismo documentado. Además, faltan los datos de seguridad del prospecto, por lo que no es posible avanzar a la revisión de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es el punto bloqueante.
- Obtener el mecanismo de acción desde DrugBank para analizar el vínculo mecanístico.
- Aclarar la indicación aprobada real, porque el registro solo indica «Metformina».
- Buscar literatura y ensayos sobre metformina en el síndrome de la persona rígida y trastornos autoinmunes afines.
- Confirmar la compatibilidad de la vía de administración y la similitud con la indicación original, hoy pendientes.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

