---
layout: default
title: Desloratadine
parent: Solo Predicción del Modelo (L5)
nav_order: 155
evidence_level: L5
indication_count: 6
---

# Desloratadine
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

# Desloratadina: De Antihistamínico para Rinitis y Urticaria a Urticaria por Frío

## Resumen en Una Frase

La desloratadina es un antihistamínico H1 de segunda generación, usado en general para los síntomas de la rinitis alérgica y la urticaria.
El modelo TxGNN predice que podría ser efectiva para la **urticaria por frío**,
con **3 ensayos clínicos** (todos completados) y **7 publicaciones** (3 de ellas ensayos clínicos aleatorizados) que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de INVIMA solo dice «DESLORATADINA»). La farmacología general la describe para rinitis y urticaria alérgicas |
| Nueva Indicación Predicha | Urticaria por frío (*cold urticaria*) |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L1 (asignado en el paquete de evidencia; los ensayos son de Fase 4, no de Fase 3) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

La desloratadina es un agonista inverso selectivo del receptor H1 de histamina (gen *HRH1*) de acción periférica. Los datos de DrugBank no traen el mecanismo de acción, pero la base de farmacología lo confirma como su blanco principal.

La urticaria por frío es una urticaria física en la que los mastocitos liberan histamina tras la exposición al frío, y esa histamina produce los habones y el prurito. Su tratamiento de primera línea son los antihistamínicos H1, el mismo mecanismo que ya se usa en la urticaria y la rinitis alérgica. Por eso el mecanismo es aplicable y la predicción es coherente.

Un punto de cautela: gran parte de la evidencia usa dosis mayores que la dosis aprobada de 5 mg (10 y 20 mg). El uso sería fuera de indicación y dependiente de la dosis. Además, el estado de indicación aprobada debe verificarse por separado, porque el registro de INVIMA no detalla las indicaciones.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Fase 4 | Completado | 30 | Estudio multicéntrico doble ciego con escalada de dosis (5, 10 y 20 mg) en urticaria adquirida por frío. Busca la dosis suficiente para inhibir los síntomas. Relevancia directa (grado A) |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Fase 4 | Completado | 33 | Estudio cruzado aleatorizado, doble ciego, controlado con placebo. Compara 5 mg frente a 20 mg en lesiones de urticaria por frío inducidas experimentalmente (termografía, volumetría y fotografía). Grado B |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Fase 4 | Completado | 150 | Compara 5 antihistamínicos en urticaria en población de Latinoamérica tropical. No indica el subtipo de urticaria, por lo que puede no ser específico de urticaria por frío. Grado B |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | ECA | J Allergy Clin Immunol | La desloratadina en dosis altas reduce el volumen de los habones y mejora los umbrales de provocación por frío frente a la dosis estándar (cruzado, con placebo) |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | ECA | Br J Dermatol | Medición del umbral crítico de temperatura en urticaria por frío con escalada de dosis de antihistamínico H1. Busca predecir la respuesta individual |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | ECA | J Dermatol Treat | Desloratadina 5 mg durante 4 días en 12 pacientes con urticaria por frío, evaluada con prueba de cubo de hielo antes y después del tratamiento |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Revisión | Drugs | Etiología, manejo y opciones de tratamiento de la urticaria crónica (contexto general) |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Revisión | Allergy | Ebastina en rinitis alérgica y urticaria crónica idiopática. Trata otro antihistamínico, por lo que es solo evidencia de contexto |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Reporte de caso | Qatar Med J | Primer caso de urticaria por frío tras anafilaxia por picadura de hormiga negra |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Reporte de caso | J Allergy Clin Immunol Pract | Urticaria por frío dependiente de alimentos, una nueva variante de urticaria física (sin resumen disponible) |

## Información de Mercado en Colombia

Hay 20 registros sanitarios en total. La tabla muestra los registros únicos de los datos recibidos, ya que varias filas estaban repetidas.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20196512 | SINNALLER® | Tableta recubierta | DESLORATADINA (el texto no detalla la indicación) |
| 20106242 | HISTALINE | Tableta recubierta | DESLORATADINA (el texto no detalla la indicación) |

También existen presentaciones en jarabe. Los fabricantes de los registros mostrados son GIMED S.A.S. (SINNALLER®) y MED LINE COLOMBIA S.A.S. (HISTALINE).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias y contraindicaciones de INVIMA no están disponibles.

Como precaución específica de esta predicción, algunos ensayos usaron dosis de hasta 20 mg, cuatro veces la dosis aprobada de 5 mg. La seguridad y la tolerabilidad en esas dosis deben confirmarse antes de cualquier uso.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Tres ensayos completados de Fase 4 y tres ECA publicados respaldan directamente el uso de desloratadina, incluso en dosis altas, en la urticaria adquirida por frío. Como el uso es fuera de indicación y depende de la dosis, se requieren salvaguardas.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones
- Confirmar si la urticaria por frío está entre las indicaciones aprobadas en Colombia
- Confirmar la seguridad y tolerabilidad de dosis superiores a 5 mg
- Verificar el subtipo de urticaria en NCT01940393 y la relación de NCT01444196 con la urticaria por frío (inferida del título y la literatura)
- Completar los datos del mecanismo de acción en DrugBank

**Otras predicciones del modelo (sin evidencia suficiente):**
- **Enfermedad de la cavidad nasal:** L4, pregunta de investigación. La evidencia son modelos animales y un estudio con loratadina; el único ensayo (NCT04088721) no confirma que el fármaco sea desloratadina.
- **Laringofaringitis aguda, dermatitis atópica recalcitrante, respuesta IgE atópica y conjuntivitis por rosácea:** L5, Hold. No hay ensayos ni literatura, y el respaldo mecanístico es débil.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

