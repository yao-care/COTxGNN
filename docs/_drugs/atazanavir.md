---
layout: default
title: Atazanavir
parent: Solo Predicción del Modelo (L5)
nav_order: 59
evidence_level: L5
indication_count: 6
---

# Atazanavir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Atazanavir: De Terapia Antirretroviral (Atazanavir+Ritonavir) a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Atazanavir es un inhibidor de la proteasa del VIH-1, y en Colombia está registrado como tabletas recubiertas de atazanavir+ritonavir. El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina** (infección por FIV en gatos).
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que es solo una señal del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ATAZANAVIR+RITONAVIR (texto del registro INVIMA; no describe una indicación clínica explícita) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, atazanavir es un inhibidor de la proteasa del VIH-1: bloquea la maduración de los viriones infecciosos. En Colombia se comercializa junto con ritonavir, y su eficacia en el VIH-1 está establecida. Mecanísticamente podría ser aplicable a la inmunodeficiencia felina, aunque esto no está verificado.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus emparentado con el VIH. Sin embargo, su proteasa difiere de la del VIH-1 en la especificidad por el sustrato. Una inhibición cruzada es plausible, pero no está demostrada.

El puntaje alto de TxGNN es solo una predicción del modelo. No hay ensayos ni literatura que la apoyen, y se trata de una indicación veterinaria, no de un uso en humanos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20066897 | VIRATAZ® TABLETAS (fabricante: Hetero Labs Limited) | Tableta recubierta | ATAZANAVIR+RITONAVIR |

Nota: el paquete de datos informa 20 registros en total, pero las entradas entregadas corresponden todas al mismo número (20066897). Se muestra una sola fila para no repetir información.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni literatura (nivel L5). Además, se refiere a una enfermedad felina, sin un vínculo terapéutico claro para uso humano.

**Para avanzar se necesita:**
- Confirmar la indicación aprobada (VIH-1) en el prospecto de INVIMA y descargar sus advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Decidir si una indicación veterinaria está dentro del alcance del programa. Si no lo está, priorizar otras predicciones.
- Revisar otras predicciones del mismo paquete que tienen más evidencia. "Complejo relacionado con el SIDA" tiene 2 ensayos de Fase 3 completados (nivel L1, Proceed with Guardrails). Corresponde a la terapia establecida del VIH-1 y no es un hallazgo de reposicionamiento; conviene confirmarla contra la etiqueta vigente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

